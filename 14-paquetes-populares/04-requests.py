import requests
# 200 get
# 201 post
# 204 eliminar

url = "https://jsonplaceholder.typicode.com/users/"

# get
r = requests.get(url, timeout=10)
# print(
#     r.status_code,
#     r.text,
# )
res = r.json()

for user in res:
    print(user["name"])




# post
user = {
    "name": "Chanchito feliz"
}
resPost = requests.post(f"{url}", data=user)
print('post',resPost.status_code)



# Put y path
resPut = requests.put(f"{url}/24", timeout=10, data=user)
print('put',resPut.status_code)


# Delete
resDel = requests.delete(f"{url}/24", timeout=10)
print('delete',resDel.status_code)



# HEADERS EN LA PETICION "CABECERAS"
apikey = "123456"
headers = {
    "Authorization": f"Bearer {apikey}", # api de validacion o token
    "Content-Type":"application/json" # indica que la cabecera es de tipo json
}
resHeaders = requests.delete(f"{url}/24", timeout=10, headers=headers)
print('delete',resDel.status_code)




