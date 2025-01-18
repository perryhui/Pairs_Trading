import blpapi
from xbbg import blp
import pandas as pd

ftse_tickers = [
    "ENT", "SMIN", "SPX", "PRU", "AAL", "CRDA", "BEZ", "TW", "GLEN", "AHT", "DPLM", 
    "IMI", "RKT", "DCC", "HSX", "EXPN", "SMT", "DGE", "BARC", "BKG", "ABF", "LLOY", 
    "RIO", "MNDI", "WPP", "LAND", "PSN", "SMDS", "BATS", "MRO", "NWG", "HWDN", "ULVR", 
    "RR", "KGF", "WEIR", "IAG", "GAW", "NG", "ANTO", "LMP", "FCIT", "CCH", "BNZL", 
    "ICG", "UTG", "IHG", "BT.A", "SBRY", "EZJ", "SGRO", "BP", "REL", "INF", "MNG", 
    "PHNX", "HLMA", "SHEL", "SDR", "ALW", "TSCO", "HLN", "CNA", "NXT", "STAN", "AZN", 
    "STJ", "BLND", "UU", "BA", "PSON", "GSK", "AV", "ITRK", "SGE", "HIK", "RTO", "PSH", 
    "BTRW", "HSBA", "WTB", "ADM", "SSE", "CTEC", "RMV", "LGEN", "SN", "EDV", "III", 
    "SVT", "IMB", "VOD", "CPG", "HL", "AAF", "LSEG", "AUTO", "MKS", "FRES", "JD",
    "BYG", "FXPO", "AML", "DSCV", "CCL", "QLT", "SAFE", "N91", "WG", "HWG", "RS1", 
    "DOCS", "TRST", "WIZZ", "CMCX", "COA", "PHI", "ITH", "IWG", "WKP", "FCSS", "SXS", 
    "INVP", "ROR", "THRG", "SRE", "BWY", "PHLL", "FGT", "BBOX", "VCT", "AJB", "IEM", 
    "PLUS", "KNOS", "SHED", "CKN", "OXIG", "STEM", "GPE", "SHC", "CWK", "GNC", "FAN", 
    "IHP", "BOY", "RHIM", "PPH", "MGAM", "HAS", "JMAT", "HET", "ABDN", "DLN", "HBR", 
    "CRST", "TPK", "HTG", "ZIG", "CCR", "EDIN", "SMWH", "GRI", "PPET", "DWL", "EMG", 
    "PAGE", "IGG", "RSW", "PHP", "SRP", "PTEC", "HFG", "SSON", "GNS", "BME", "GRG", 
    "MNKS", "TATE", "LRE", "ESP", "TEM", "CCC", "MYI", "PRSR", "PCT", "FEV", "BAG", 
    "DNLM", "INCH", "ALPH", "JEDT", "CURY", "CGT", "OSB", "BBY", "SVS", "HSL", "MRCH", 
    "EOT", "JMG", "ATG", "BRGE", "PAG", "CTY", "JAM", "LWDB", "JGGI", "HILS", "BRSC", 
    "SSPG", "ITV", "ELM", "BBH", "MUT", "OCDO", "MRC", "AGT", "BRWM", "SAIN", "SDP", 
    "BOWL", "FUTR", "NESF", "GFTU", "THRL", "IBST", "ATT", "HTWS", "IDS", "HMSO", "FGP", 
    "VEIL", "TRY", "TMPL", "TIFS", "SYNC", "SPT", "SOI", "PNN", "PFD", "PCFT", "MSLH", 
    "MAB", "JDW", "GSCT", "DLG", "DGN", "BREE", "BMY", "ALFA", "AGR", "ENOG", "RAT", 
    "QQ", "KIE", "NCC", "CHG", "ESNT", "BNKR", "BYIT", "USA", "PNL", "MOON", "RCP", 
    "ASHM", "FSG", "DOM", "BGFD", "BCG", "WWH", "PIN", "FEML", "3IN", "SCT", "JFJ", "TEP", 
    "MTO", "VSVS", "RICA", "HVPE", "HGT", "MGNS", "JTC", "SUPR", "BSIF", "FSV", "DRX", 
    "RWI", "NBPE", "FSFL", "BAB", "ICGT", "SNR", "TBCG", "GEN", "TRN", "MONY", "ASL", 
    "HICL", "VTY", "BRBY", "MCG", "GDWN", "CLDN", "SPI", "PAY", "INPP", "TCAP", "GROW", 
    "KLR", "VOF", "BUT", "XPS", "BGEO", "FRAS", "MTRO", "TFIF", "JII", "FOUR", "APAX", 
    "UKW", "MEGP", "BBGI", "WOSG", "SEIT", "RPI", "JUST", "FGEN", "EWI", "AO", "ROO", 
    "SEQI", "GCP", "BHMG", "DEC", "PETS", "CHRY", "ESCT", "IPO", "ONT", "JUP", "TRIG", 
    "BPT", "NAS", "WPS", "HOC", "HRI", "BAKK", "BVIC","AGVI", "AAS", "AAIF", "ADIG", "AEI", "ASLI", "ANII", "API", "AUSC", "AEWU", "AEP", "APN", "APTD", 
    "AIE", "ASC", "AUGM", "ARR", "AJOT", "AVON", "BGCG", "BGEU", "BGS", "BGUK", "BIOG", "BRAI", "BERI", 
    "BRFI", "BRLA", "BOOT", "BASC", "CABP", "CPI", "CAPD", "CNE", "CARD", "CRT", "CARR", "CCJI", "CWR", 
    "CSN", "CLIG", "CBG", "CLI", "COST", "CYN", "NCYF", "CTPE", "CTUK", "CHI", "CREI", "CVCG", "DLAR", 
    "DFS", "DGI9", "DIVI", "DORE", "DIG", "EGL", "ECOR", "ENQ", "ECEL", "EAT", "EVOK", "FDM", "FAS", 
    "FJV", "FORT", "FOXT", "FSTA", "FCH", "GFRD", "GABI", "GOT", "GSF", "GMS", "GYM", "HFD", "HEAD", 
    "HLCL", "HFEL", "HHI", "HINT", "HOT", "HSW", "IGC", "IBT", "IPF", "IAT", "BIPS", "IGET", "IPU", "FSJ", 
    "JAGI", "JCGI", "JCH", "JEGI", "JARA", "JEMI", "JUGI", "JUSC", "KMR", "KPC", "LABS", "LTI", "LIO", 
    "LWI", "LSL", "LUCE", "MGCI", "MACF", "MAJE", "MNL", "MARS", "MNP", "MCB", "MER", "MWY", "MCT", "GLE", "MMIT", 
    "MTE", "MTU", "MOTR", "NRR", "NAVF", "NXR", "NAIT", "OCN", "ORIT", "OIT", 
    "OTB", "OIG", "OXB", "PAC", "PCA", "PINT", "PBEE", "PDL", "PFC", "PHAR", 
    "PSDL", "PCTN", "PINE", "PCGH", "PRV", "PRTC", "PZC", "RNK", "RCH", "RECI", 
    "REC", "RGL", "RESI", "RCDO", "RIII", "RSE", "RMII", "RWA", "SUS", "SBRE", 
    "SAGA", "ATR", "SERE", "SCF", "SJG", "SREI", "SCP", "INOV", "SST", "STB", 
    "SSIT", "SFR", "SHRS", "SHI", "SNWS", "SOHO", "SDY", "SWEF", "SEC", "STS", 
    "STVG", "SYNT", "TMIP", "TPT", "TET", "TRI", "TTG", "TLW", "SMIF", "ULTP", 
    "UEM", "VIP", "VANQ", "ENRG", "VID", "VNH", "VP.", "VSL", "WHR", "WIX", "XAR", 
    "XPP", "ZTF"
]



def data_processing(ftse_tickers):
    ftse_updated = []
    for ticker in ftse_tickers:
        ftse_updated.append(ticker + " LN Equity")  # Add ' LN Equity' to each ticker
    return ftse_updated


ftse_updated = data_processing(ftse_tickers)

# Fields for price, market data, risk, and volatility
fields_price = [
    'PX_LAST',         # Last price
    'PX_OPEN',         # Open price
    'PX_HIGH',         # High price
    'PX_LOW',          # Low price
    'PX_CLOSE',        # Close price
    'PX_ADJ_CLOSE',    # Adjusted close price
    'VOLUME',          # Trading volume
    'VOLUME_AVG',      # Average volume
    'OPEN_INT',         # Open interest
    'VOLATILITY_30D',   # 30-day volatility
    'BETA'             # Beta coefficient (systematic risk)
]

# Fields for financial ratios 
fields_ratio = [
    'PE_RATIO',        # Price-to-earnings ratio
    'PB_RATIO',        # Price-to-book ratio
    'DIVIDEND_YIELD',  # Dividend yield
    'ROE',             # Return on equity
    'ROA',             # Return on assets
    'DEBT_TO_EQUITY'   # Debt-to-equity ratio
]


Start_date = '2010-01-01'
End_date = '2023-12-31'

# Fetch historical data
historical_tick_data = blp.bdh(tickers=ftse_updated, flds=fields_price, start_date=Start_date, end_date=End_date)
historical_ratio = blp.bdh(tickers=ftse_updated, flds=fields_ratio, start_date=Start_date, end_date=End_date)

# Check the returned dataframes (optional)
print(historical_tick_data.head())
print(historical_ratio.head())

# Save data to a CSV file
file_name_price = f'ticker_data_{Start_date}_{End_date}.csv'
historical_tick_data.to_csv(file_name_price)

file_name_ratio = f'financial_ratio_data_{Start_date}_{End_date}.csv'
historical_ratio.to_csv(file_name_ratio)

