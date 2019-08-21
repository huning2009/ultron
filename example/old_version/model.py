# -*- coding: utf-8 -*-
from sqlalchemy import BigInteger, Column, DateTime, Float, Index, Integer, String, Text, Boolean, text, JSON,TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

class IndustryComponents(Base):
    __tablename__ = 'industry'
    trade_date = Column(DateTime, primary_key=True, nullable=False)
    code = Column(Integer, primary_key=True, nullable=False)
    industry = Column(String(30))
    industryID = Column(BigInteger)
    industrySymbol = Column(String(20))
    industryID1 = Column(BigInteger)
    industryName1 = Column(String(20))
    industryID2 = Column(BigInteger)
    industryName2 = Column(String(20))
    industryID3 = Column(BigInteger)
    industryName3 = Column(String(20))
    industryID4 = Column(BigInteger)
    industryName4 = Column(String(20))
    
class IndexComponents(Base):
    __tablename__ = 'index_components'
    trade_date = Column(DateTime, primary_key=True, nullable=False)
    code = Column(Integer, primary_key=True, nullable=False)
    effDate = Column(DateTime)
    indexShortName = Column(String(16))
    indexCode = Column(String(16))
    secShortName = Column(String(16))
    exchangeCD = Column(String(16)) 
    weight = Column(Float(53))
  
    
class Min5DailyHighFrequency(Base):
    __tablename__ = '5min_daily_high_frequency'
    trade_date = Column(DateTime, primary_key=True, nullable=False)
    code = Column(Integer, primary_key=True, nullable=False)
    flow_in_ratio1_20 = Column(Float(53))
    improved_reversal_20 = Column(Float(53))
    trend_strength_20 = Column(Float(53))
    volume_price_corr_20 = Column(Float(53))
    volume_ratio_1000 = Column(Float(53))
    volume_ratio_1030 = Column(Float(53))
    volume_ratio_1100 = Column(Float(53))
    volume_ratio_1130 = Column(Float(53))
    volume_ratio_1330 = Column(Float(53))
    volume_ratio_1400 = Column(Float(53))
    volume_ratio_1430 = Column(Float(53))
    volume_ratio_1500 = Column(Float(53))
    
    
class Experimental(Base):
    __tablename__ = 'experimental'
    trade_date = Column(DateTime, primary_key=True, nullable=False)
    code = Column(String, primary_key=True, nullable=False)
    ROEAfterNonRecurring = Column(Float(53))
    CHV = Column(Float(53))
    DROE = Column(Float(53))
    IVR = Column(Float(53))
    EPAfterNonRecurring = Column(Float(53))
    DROEAfterNonRecurring = Column(Float(53))
    CFinc1 = Column(Float(53))
    Revenue = Column(Float(53))
    DRevenue = Column(Float(53))
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
    
    
    

class Market(Base):
    __tablename__ = 'market'
    __table_args__ = (
        Index('market_idx', 'trade_date', 'code', unique=True),
    )

    trade_date = Column(DateTime, primary_key=True, nullable=False)
    code = Column(String, primary_key=True, nullable=False)
    secShortName = Column(String(10))
    exchangeCD = Column(String(4))
    preClosePrice = Column(Float(53))
    actPreClosePrice = Column(Float(53))
    openPrice = Column(Float(53))
    highestPrice = Column(Float(53))
    lowestPrice = Column(Float(53))
    closePrice = Column(Float(53))
    turnoverVol = Column(BigInteger)
    turnoverValue = Column(Float(53))
    dealAmount = Column(BigInteger)
    turnoverRate = Column(Float(53))
    accumAdjFactor = Column(Float(53))
    negMarketValue = Column(Float(53))
    marketValue = Column(Float(53))
    chgPct = Column(Float(53))
    PE = Column(Float(53))
    PE1 = Column(Float(53))
    PB = Column(Float(53))
    isOpen = Column(Integer)
    vwap = Column(Float(53))
    
class RiskExposure(Base):
    __tablename__ = 'risk_exposure'
    trade_date =  Column(DateTime, primary_key=True, nullable=False)
    code =  Column(String, primary_key=True, nullable=False)
    BETA = Column(Float(53))
    MOMENTUM = Column(Float(53))
    SIZE = Column(Float(53))
    EARNYILD = Column(Float(53))
    RESVOL = Column(Float(53))
    GROWTH = Column(Float(53))
    BTOP = Column(Float(53))
    LEVERAGE = Column(Float(53))
    LIQUIDTY = Column(Float(53))
    SIZENL = Column(Float(53))
    Bank = Column(Float(53))
    RealEstate = Column(Float(53))
    Health = Column(Float(53))
    Transportation = Column(Float(53))
    Mining = Column(Float(53))
    NonFerMetal = Column(Float(53))
    HouseApp = Column(Float(53))
    LeiService = Column(Float(53))
    MachiEquip = Column(Float(53))
    BuildDeco = Column(Float(53))
    CommeTrade = Column(Float(53))
    CONMAT = Column(Float(53))
    Auto = Column(Float(53))
    Textile = Column(Float(53))
    FoodBever = Column(Float(53))
    Electronics = Column(Float(53))
    Computer = Column(Float(53))
    LightIndus = Column(Float(53))
    Utilities = Column(Float(53))
    Telecom = Column(Float(53))
    AgriForest = Column(Float(53))
    CHEM = Column(Float(53))
    Media = Column(Float(53))
    IronSteel = Column(Float(53))
    NonBankFinan = Column(Float(53))
    ELECEQP = Column(Float(53))
    AERODEF = Column(Float(53))
    Conglomerates = Column(Float(53))
    COUNTRY = Column(Float(53))
    updateTime = Column(DateTime)