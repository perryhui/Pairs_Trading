import blpapi
from xbbg import blp
import pandas as pd


ftse_tickers = ["ADM", "AAF", "ALW", "AAL", "ANTO", "AHT", "ABF", "AZN", "AUTO", "AV", 
    "BA", "BARC", "BTRW", "BEZ", "BKG", "BP", "BATS", "BLND", "BT-A", "BNZL",
    "CNA", "CCH", "CPG", "CTEC", "CRDA", "DCC", "DGE", "DPLM", "EDV", "ENT", 
    "EZJ", "EXPN", "FCIT", "FRES", "GAW", "GLEN", "GSK", "HLN", "HLMA", "HL",
    "HIK", "HSX", "HWDN", "HSBA", "IHG", "IMI", "IMB", "INF", "ICG", "IAG", 
    "ITRK", "JD", "KGF", "LAND", "LGEN", "LLOY", "LMP", "LSEG", "MNG", "MKS", 
    "MRO", "MNDI", "NG", "NWG", "NXT", "PSON", "PSH", "PSN", "PHNX", "PRU", 
    "RKT", "REL", "RTO", "RMV", "RIO", "RR", "SGE", "SBRY", "SDR", "SMT", 
    "SGRO", "SVT", "SHEL", "SMDS", "SMIN", "SN", "SPX", "SSE", "STAN", 
    "STJ", "TW", "TSCO", "ULVR", "UU", "UTG", "VOD", "WEIR", "WTB", "WPP", 
    "3IN", "FOUR", "ABDN", "ALFA", "ATT", "ALPH", "AO", "APAX", "ASHM", "DGN",
    "AGR", "AML", "ATG", "AGT", "BME", "BAB", "BGFD", "USA", "BAKK", "BBY", 
    "BCG", "BNKR", "BGEO", "BAG", "BBGI", "AJB", "BBH", "BWY", "BHMG", "BYG", 
    "BRGE", "BRSC", "THRG", "BRWM", "BMY", "BSIF", "BOY", "BREE", "BPT", "BVIC", 
    "BUT", "BRBY", "BYIT", "CCR", "CLDN", "CGT", "CCL", "CHG", "CHRY", "CTY", 
    "CKN", "CMCX", "COA", "CCC", "CWK", "CRST", "CURY", "ROO", "DLN", "DLG", 
    "DSCV", "DEC", "DOM", "DWL", "DRX", "DOCS", "DNLM", "EDIN", "EWI", "ELM", 
    "ESP", "ENOG", "ESNT", "EOT", "ESCT", "FXPO", "FCSS", "FEML", "FEV", "FSV", 
    "FGT", "FGP", "FSG", "FSFL", "FRAS", "FUTR", "GCP", "GEN", "GNS", "GSCT", 
    "GDWN", "GFTU", "GRI", "GPE", "UKW", "GNC", "GRG", "HMSO", "HBR", "HVPE", 
    "HWG", "HAS", "HTWS", "HET", "HSL", "HRI", "HGT", "HICL", "HILS", "HFG", 
    "HOC", "BOWL", "HTG", "IBST", "ICGT", "IGG", "IEM", "INCH", "IHP", "IDS", 
    "INPP", "INVP", "IPO", "ITH", "ITV", "IWG", "JLEN", "JMAT", "JAM", "JMG", 
    "JEDT", "JGGI", "JII", "JFJ", "JTC", "JUP", "JUST", "KNOS", "KLR", "KIE", 
    "LRE", "LWDB", "EMG", "MSLH", "MEGP", "MRC", "MRCH", "MTRO", "MAB", "MTO", 
    "MCG", "GROW", "MONY", "MNKS", "MOON", "MGAM", "MGNS", "MUT", "MYI", "NBPE", 
    "NCC", "NESF", "N91", "NAS", "OCDO", "OSB", "OXIG", "ONT", "PHI", "PAGE", 
    "PIN", "PAG", "PPET", "PAY", "PNN", "PNL", "PHLL", "PETS", "PTEC", "PLUS",
    "PCFT", "PCT", "PPH", "PFD", "PHP", "PRS", "QQ", "QLT", "RPI", "RAT", 
    "RWI", "RSW", "RHIM", "RCP", "ROR", "RS1", "RICA", "SAFE", "SVS", "SDP", 
    "SOI", "SAIN", "SEIT", "SNR", "SEQI", "SRP", "SHC", "SRE", "SSON", "SCT", 
    "SXS", "SPI", "SPT", "SSPG", "STEM", "SUPR", "SYNC", "THRL", "TATE", "TBCG",
    "TEP", "TMPL", "TEM", "TRIG", "TIFS", "TCAP", "TRN", "TPK", "BBOX", "TRY", 
    "TRST", "TFIF", "SHED", "VSVS", "VCT", "VEIL", "VOF", "VTY", "FAN", "WPS", 
    "WOSG", "JDW", "SMWH", "WIZZ", "WG", "WKP", "WWH", "XPS", "ZIG"
]  

def data_processing(ftse_tickers):
    ftse_updated = []
    for ticker in ftse_tickers:
        ftse_updated.append(ticker + " LN Equity")  # Add ' LN Equity' to each ticker
    return ftse_updated


ftse_updated = data_processing(ftse_tickers)

fields_price = ['Last_Price']
fields_volume = ['VOLUME', 'ADVOLUME', 'VOLUME_3M', 'VOLUME_TODAY']
fields_ratio = [
    'PE_RATIO', 'PB_RATIO', 'DIVIDEND_YIELD', 'ROE', 'ROA', 'DEBT_TO_EQUITY'
]
Start_date = '2010-01-01'
End_date = '2023-12-31'

# Fetch historical data
historical_tick_data = blp.bdh(tickers=ftse_updated, flds=fields_price, start_date=Start_date, end_date=End_date)
historical_volume = blp.bdh(tickers = ftse_updated, flds = fields_volume, start_date = Start_date, end_date = End_date)
historical_ratio = blp.bdh(tickers = ftse_updated, flds = fields_ratio, start_date = Start_date, end_date = End_date)


# Save data to a CSV file
file_name_price = f'ticker_data_{Start_date}_{End_date}.csv'
historical_tick_data.to_csv(file_name_price)

file_name_volume = f'volume_data_{Start_date}_{End_date}.csv'
historical_volume.to_csv(file_name_volume)

file_name_ratio = f'financial_ratio_data_{Start_date}_{End_date}.csv'
historical_volume.to_csv(file_name_ratio)


