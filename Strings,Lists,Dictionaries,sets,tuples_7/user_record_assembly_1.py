raw_user_record = " 10827 ; aLeXanDer_vLaDimiRov ; mInSk ; ACTIVE "
#splitting by ;
user_record = raw_user_record.split(';')
#cleansing from whitespaces
cleansed_user_record = []
for line in user_record:
    stripped_line = line.strip()
    cleansed_user_record.append(stripped_line)
#adding UID- prefix
cleansed_user_record[0]=f"UID-{cleansed_user_record[0]}"
#formatting user name
cleansed_user_record[1]=cleansed_user_record[1].replace("_"," ")
cleansed_user_record[1]=cleansed_user_record[1].title()
#formatting city name
cleansed_user_record[2]=cleansed_user_record[2].upper()
#formatting user status
cleansed_user_record[3]=cleansed_user_record[3].lower()
#joining and printing
processed_user_record = " | ".join(cleansed_user_record)
print(f"Нормализованная запись: {processed_user_record}")
