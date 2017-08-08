USE [PPODB]
GO
/****** Object:  StoredProcedure [dbo].[usp_scCheckContractDelete]    Script Date: 2017/1/11 16:45:29 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO


/*     
    文  件  名 ：[PPODB].[dbo].[usp_scCheckContractDelete]   
    
    2016-10-10 (周一) 12:11 He, Zhi Yong /GET/IT <hezhiy@esquel.com>   为处理用户取消外发合同明细时出现问题   
    
    创  建  人 ：chenjh    
    创建日期 ：2004-09-03    
    修  改  人 ：    
    修改原因 ：--请求ID : 281255 tracy tan 2016-12-20    --请求ID：287472 Henry Wang 2017-01-11
    修改日期 ：    
       
    功能描述 ： 该存储过程用来判断合同明细记录是否可以删除    
       
    参        数 ：    
                @Process_Type       外加工类型    
                @Contract_No        合同号    
    @Contract_ID        合同明细记录ID    
                @Result             返回结果 output    
    处理流程 ：  判断该合同ITEM能否删除，若不能则返回不能删除的原因,若能删除 返回'OK'    
    参考文档 ：     
*/     
ALTER PROCEDURE [dbo].[usp_scCheckContractDelete]    
(@Process_Type varchar(10),@Contract_No varchar(20),@Contract_ID int,@Result varchar(100) output)    
AS    
set nocount on     
    
set @Result='未知错误！'    
    
    --收付上传OAS
  if exists(select 1 from scReceipt (nolock) where ContractNo=@Contract_No and ReceiptID=@Contract_ID)    
  begin    
    set @Result='该合同明细已有收付记录,不能删除!'    
    return    
  end    
if @Process_Type in ('TW','YD','LT') --并线，染纱，络筒，整浆 在YARNTASK中    
begin    
  --取消或完成不能删除    
  if exists(select 1 from scYarnTask (nolock) where Contract_No=@Contract_No and SC_Yarn_ID=@Contract_ID and Contract_Status in ('取消','完成'))    
  begin    
    set @Result='该合同明细已完成或已取消,不能删除!'    
    return    
  end    
    
  if exists (select 1 from wmsdb..ysApply a (nolock)     
             inner join scYarnTask b (nolock) on a.SC_Contract_NO=b.Contract_No and a.Job_No=b.Job_No and a.GF_ID=b.GF_ID    
             where b.SC_Yarn_ID=@Contract_ID and a.Is_Agreed<>'N' and a.Status<>'已取消')    
  begin    
    set @Result='该合同明细已经申领纱，不能删除！'    
    return    
  end    
    
  if exists (select 1 from wmsdb..ysOut a (nolock)     
             inner join scYarnTask b (nolock) on a.SC_Contract_NO=b.Contract_No and a.Job_No=b.Job_No and a.GF_ID=b.GF_ID    
             where b.SC_Yarn_ID=@Contract_ID )    
  begin    
    set @Result='该合同明细已经发纱，不能删除！'    
    return    
  end    
    
  if exists (select 1 from wmsdb..ysIn a (nolock)     
             inner join scYarnTask b (nolock) on a.SC_Contract_NO=b.Contract_No and a.Yarn_Type=b.Yarn_Type and a.Yarn_Count=b.Yarn_Count and a.Color_Code=b.Color_Code    
             where b.SC_Yarn_ID=@Contract_ID)    
  begin    
    set @Result='该合同明细已有成品纱入仓，不能删除！'    
    return    
  end    
      
end    
else    
begin    
  --取消或完成不能删除    
  if exists(select 1 from scFabricTask (nolock) where Contract_No=@Contract_No and SC_Fabric_ID=@Contract_ID and Contract_Status in ('取消','完成'))    
  begin    
    set @Result='该合同明细已完成或已取消,不能删除!'    
    return    
  end      
end    
    
    
if @Process_Type in ('PR','WV','PW','FN') --整浆，织布，整浆织，后整    
begin    
    if exists (select 1 from wmsdb..fsInDtl a (nolock)     
             inner join wmsdb..fsItem c (nolock) on a.Fs_Item_NO=c.Fs_Item_NO    
             inner join scFabricTask b (nolock) on a.Contract_No=b.Contract_No and a.Job_No=b.Job_No and c.GF_ID=b.GF_ID    
             where b.SC_Fabric_ID=@Contract_ID)      
    begin    
      set @Result='布仓已有该合同记录，不能删除！'    
      return    
    end      
    
    --FN已收布    
    if @Process_Type='FN' and exists (select 1 from FNMDB.dbo.fnReceiveDtl a with(nolock)    
                                      inner join scFabricTask b with(nolock) on a.SC_Contract_No=b.Contract_No and a.Job_No=b.Job_No and a.GF_ID=b.GF_ID and     
                                        a.Note_NO = b.Note_NO    
                                      where b.SC_Fabric_ID=@Contract_ID)    
    begin    
      set @Result='该合同布已返回后整理，不能删除！'    
      return     
    end    

	if @Process_Type='FN' and exists (select 1 
		                              from FNMDB.dbo.uvw_fnPay a with(nolock)    
                                         inner join ppodb..scFabricTask b with(nolock) on a.SC_Contract_No=b.Contract_No and a.Job_No=b.Job_No and a.GF_ID=b.GF_ID 
                                      where b.SC_Fabric_ID=@Contract_ID)    
    begin    
      set @Result='该合同布已经送布，不能删除！ 请让后整进行退布收布操作'    
      return     
    end 
    
    if exists (select 1 from WVMDB..wvWeaveBeamOut a     
             inner join WVMDB..wvCard b on a.WV_Card=b.WV_Card        
             where b.SC_Weaving_ID=@Contract_ID and a.Destination='SC')    
    begin    
       set @Result='准备间已有出轴记录，不能删除！'    
       return    
    end    
    
    if @Process_Type in ('PR','PW','WV') --整浆织可能从仓库发纱出去    
    begin     
        if exists (select 1 from wmsdb..ysApply a (nolock)      
             inner join scFabricTask b (nolock) on a.SC_Contract_NO=b.Contract_No and a.Job_No=b.Job_No and a.GF_ID=b.GF_ID    
             where b.SC_Fabric_ID=@Contract_ID and a.Is_Agreed<>'N' and a.Status<>'已取消' and a.[Status]<>'已完成')    
        begin    
            set @Result='该合同明细已经申领纱，不能删除！'    
            return    
        end    
    
        if exists (select 1
					from (
									select sum(quantity) as Out_Qty from wmsdb..ysOut a (nolock)    
										inner join scFabricTask b (nolock) on a.SC_Contract_NO=b.Contract_No and a.Job_No=b.Job_No and a.GF_ID=b.GF_ID    
									where b.SC_Fabric_ID=@Contract_ID ) A

							left OUTER JOIN (
									select  sum(quantity) as return_Qty  from wmsdb..ysIN a (nolock)    
										inner join scFabricTask b (nolock) on a.SC_Contract_NO=b.Contract_No and a.sc_contract_id=b.SC_Fabric_ID
									where b.SC_Fabric_ID=@Contract_ID and In_type like '%外发加工退%' ) B
							on 1=1
							left OUTER JOIN (
									select  quantity as sc_Qty
									from scFabricTask b 
									where b.SC_Fabric_ID=@Contract_ID ) c
							on 1=1
					where ( case when Out_Qty>sc_Qty then sc_Qty else Out_Qty end  -   isnull(return_Qty,0))/case when Out_Qty>sc_Qty then sc_Qty else Out_Qty end>0.1 and @Contract_ID not in (187995,188321,188314)  --请求ID : 281255 tracy tan   
							  ---如果发纱量比本次取消的量大， 就检查 退货的量有没 本次取消的量大，有则可以取消
					)    
        begin    
			set @Result='该合同明细已经发纱且没退完纱，不能删除！'    
            return    
        end    
    end    
    
end    
     
if @Process_Type in ('BS','PT') --床单布、印花布 从成品仓出布    
begin    
    if exists (select 1 from wmsdb..fsOut (nolock) where Ship_Plan_No like 'SC%' and Ship_Plan_ID=@Contract_ID)     
    begin    
        set @Result='成品仓已经出布，不能删除！'    
        return     
    end    
    
    if exists (select 1 from wmsdb..fsshipprepare (nolock) where Ship_Plan_No like 'SC%' and Ship_Plan_ID=@Contract_ID)     
    begin    
        set @Result='成品仓已经组货，不能删除！'    
        return     
    end    
end    
    
set @Result='OK'  
