import itertools
import pandas as pd

from termcolor import colored

def main():
    
    def run(simulations, df):
        
        for ticker in range(3,len(df.columns)):
            
            print("[INFO]: GENERATING PORTFOLIO COMBINATIONS OF SIZE", ticker)
            combinations = list(itertools.combinations(df.columns, ticker))
            
            for combos in combinations:
                
                print(colored("[INFO]:", "green"),"GENERATING PORTFOLIO WITH TICKERS:", combos)
                specific_portfolio = df[list(combos)]
                
                for simulation in range(simulations):
                    
                    if simulation % 10000 == 0:
                        print("simulation:", simulation)
                        
                print("")
       
    simulations = 40000
    df = pd.read_csv("sample_stocks.csv", index_col = 0).dropna().pct_change().dropna()
    run(simulations, df)
        
if __name__ == "__main__":
    main()