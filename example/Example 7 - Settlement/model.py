# -*- coding: utf-8 -*-
from sqlalchemy import BigInteger, Column, DateTime, Float, Index, Integer, String, Text, Boolean, text, JSON,TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

class Experimental(Base):
    __tablename__ = 'experimental'
    trade_date = Column(DateTime, primary_key=True, nullable=False)
    code = Column(Integer, primary_key=True, nullable=False)
    CHV = Column(Float(53))
    DROE = Column(Float(53)
    IVR = Column(Float(53))
    ROEAfterNonRecurring = Column(Float(53))
    EPAfterNonRecurring = Column(Float(53))
    DROEAfterNonRecurring = Column(Float(53))
    CFinc1 = Column(Float(53))
    xueqiu_hotness = Column(Float(53))
    roe_q = Column(Float(53))
    eps_q = Column(Float(53)
    val_q = Column(Float(53))
    cfinc1_q = Column(Float(53))
    ep_q = Column(Float(53))
    ep_q_d_1w = Column(Float(53))
    ev = Column(Float(53))
    liq = Column(Float(53))
    pure_liq_0 = Column(Float(53))
    pure_liq_1 = Column(Float(53)
    pure_liq_2 = Column(Float(53))
    pure_liq_3 = Column(Float(53))
    pure_liq_4 = Column(Float(53))
    pe_hist60 = Column(Float(53))
    cap_liq = Column(Float(53))
    pure_cap_liq_0 = Column(Float(53))
    pure_cap_liq_1 = Column(Float(53))
    pure_cap_liq_2 = Column(Float(53)
    pure_cap_liq_3 = Column(Float(53))
    pure_cap_liq_4 = Column(Float(53))
    apm_10 = Column(Float(53))
    apm_20 = Column(Float(53))
    amh_10 = Column(Float(53))
    amh_20 = Column(Float(53))
    mix_liq = Column(Float(53))
    mix_cap_liq = Column(Float(53))
    high_mtm_20 = Column(Float(53)
    low_mtm_20 = Column(Float(53))
    ideal_mtm_20 = Column(Float(53))
    chlc = Column(Float(53))
    chlv = Column(Float(53))
    ccv = Column(Float(53))
    chv = Column(Float(53))
    clv = Column(Float(53))
    cvvwap = Column(Float(53))
    idl_mtm_20 = Column(Float(53))
    smart_q = Column(Float(53))
    roep = Column(Float(53))
    roep_q = Column(Float(53))
    con_roep = Column(Float(53))
    con_roep_rolling = Column(Float(53))
    rvol = Column(Float(53))
    rskew = Column(Float(53))
    rkurt = Column(Float(53))
    rhhi = Column(Float(53))
    vvol = Column(Float(53))
    vskew = Column(Float(53))
    vkurt = Column(Float(53))
    vhhi = Column(Float(53))
    rvol_std = Column(Float(53))
    rskew_std = Column(Float(53))
    rkurt_std = Column(Float(53))
    rhhi_std = Column(Float(53))
    vvol_std = Column(Float(53))
    vskew_std = Column(Float(53))                     
    vkurt_std = Column(Float(53))
    vhhi_std = Column(Float(53))
    ivr_day = Column(Float(53))
    ivr_bar60 = Column(Float(53))
    ivr_bar30 = Column(Float(53))
    CFinc1_new = Column(Float(53))
    cfinc1_rev = Column(Float(53))
    revenue = Column(Float(53))
    drevenue = Column(Float(53))
    cfinc2 = Column(Float(53))
    retd = Column(Float(53))
    abs_retd = Column(Float(53))
    vretd = Column(Float(53))
    abs_vretd = Column(Float(53))
    retd_bar5 = Column(Float(53))
    vretd_bar5 = Column(Float(53))
    retd_bar15 = Column(Float(53))
    vretd_bar15 = Column(Float(53))
                   