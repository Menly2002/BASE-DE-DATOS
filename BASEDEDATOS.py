import streamlit as st
from supabase import create_client

# CONEXION
url = "https://ohqvjyytcbwonzkjksxm.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im9ocXZqeXl0Y2J3b256a2prc3htIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODE4MTcxOTgsImV4cCI6MjA5NzM5MzE5OH0.kr3f6C9Skq_IS_1r1PcoekHJalnlgRGFfGfJEhncckw"

supabase = create_client(url, key)

st.title("CRUD DE ALUMNOS")

menu = st.sidebar.selectbox(
    "Seleccione",
    ["Crear","Consultar","Actualizar","Eliminar"]
)

# CREAR
if menu == "Crear":

    st.subheader("Registrar Alumno")

    dni = st.text_input("DNI")
    ap_pat = st.text_input("Apellido Paterno")
    ap_mat = st.text_input("Apellido Materno")
    nombre = st.text_input("Nombre")

    sexo = st.selectbox(
        "Sexo",
        ["Masculino","Femenino"]
    )

    edad = st.number_input(
        "Edad",
        min_value=1,
        max_value=100
    )

    if st.button("Guardar"):

        datos = {
            "dni": dni,
            "apellido_pat": ap_pat,
            "apellido_mat": ap_mat,
            "nombre": nombre,
            "sexo": sexo,
            "edad": edad
        }

        supabase.table("ALUMNOS").insert(datos).execute()

        st.success("Alumno registrado")

# CONSULTAR
elif menu == "Consultar":

    st.subheader("Lista de alumnos")

    resultado = supabase.table(
        "ALUMNOS"
    ).select("*").execute()

    st.dataframe(resultado.data)

# ACTUALIZAR
elif menu == "Actualizar":

    dni = st.text_input("DNI a actualizar")

    nueva_edad = st.number_input(
        "Nueva edad",
        min_value=1,
        max_value=100
    )

    if st.button("Actualizar"):

        supabase.table("ALUMNOS")\
        .update({"edad": nueva_edad})\
        .eq("dni", dni)\
        .execute()

        st.success("Registro actualizado")

# ELIMINAR
elif menu == "Eliminar":

    dni = st.text_input("DNI a eliminar")

    if st.button("Eliminar"):

        supabase.table("ALUMNOS")\
        .delete()\
        .eq("dni", dni)\
        .execute()

        st.success("Registro eliminado")
