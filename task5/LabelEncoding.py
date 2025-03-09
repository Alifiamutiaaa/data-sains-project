import pandas as pd

dataset = "data-pengurus-rt-dan-rw-tahun-2020.csv"
df = pd.read_csv(dataset, encoding='cp1252')
to_drop = ['Kode Kecamatan','Kecamatan', 'Kode Kelurahan', 'Kelurahan']
df = df.drop(to_drop, axis=1)

X = df['Jabatan'].values.reshape(-1,1)

from sklearn.preprocessing import OneHotEncoder
onehot_encoder = OneHotEncoder()
X = onehot_encoder.fit_transform(X).toarray()
print("One Hot Encoder")
print(X)

print(onehot_encoder.categories_)

df_onehot= pd.DataFrame(X, columns=[str(i) for i in range(X.shape[1])])
print(df_onehot.head(20))

df=pd.concat([df_onehot,df], axis=1)
print("menggabungkan dataframe")
print(df.head(20))

df = df.drop(['Jabatan'], axis=1)
print("Buang Atribut Country karena Direpresentasikan dengan OneHotEncoder")
print(df.head(20))


#print(df.head(20))
