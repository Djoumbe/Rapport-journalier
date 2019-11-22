import pandas
pandas.options.display.max_rows = 10

df = pandas.read_excel("/home/utilisateur/Téléchargements/autompg.xlsx", sep = '\t', header = 0)

print (df)
print (df.shape)
print (df.head())
print (df.origine)
print (df.mpg)
print (df["origine"].argsort())