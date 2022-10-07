import pandas as pd; import requests; from csv import DictReader

def TableScrape(url, tbindex, filename):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.47",}
    df = pd.read_html(requests.get(url, headers=headers).text, flavor = "lxml")
    pd.DataFrame(df[int(tbindex)]).to_csv(filename + '.csv', index=False)

def DataSetFormat(filename):
    cab = ['Classificacao', 'Equipa', 'Jogos', 'Vitorias', 'Empates', 'Derrotas', 'Golos Marcados', 'Golos Sofridos', 'Diferenca de Golos', 'Pontos', 'Pontos por Jogo','Vitorias em Casa', 'Empates em Casa', 'Derrotas em Casa', 'Golos Marcados em Casa', 'Golos Sofridos em Casa', 'Vitorias Fora', 'Empates Fora', 'Derrotas Fora', 'Golos Marcados Fora', 'Golos Sofridos Fora' ]
    df = pd.read_csv (filename + '.csv')
    df.drop(['10', '12', '18', '19', '20', '21'], inplace = True, axis = 1)
    df = df.dropna()
    df.reset_index(drop = True, inplace = True)
    df['0'] = df['0'].astype(float).astype(int)
    df.to_csv(filename + '.csv', index= False, header = cab)

def ListScrape(listfile):
    with open(listfile, 'r') as my_file:
        csv_dict_reader = DictReader(my_file)
        for row in csv_dict_reader:
            TableScrape(row['link'], row['tindex'], row["camp"])
            DataSetFormat(row['camp'])

ListScrape('scrapelist.csv')