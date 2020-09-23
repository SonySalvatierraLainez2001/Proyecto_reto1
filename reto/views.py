from django.shortcuts import render


# Create your views here.
html_base = """
    <h1> Unidad Educativa Eloy Alfaro</h1>
    <ul>
        <li>   <a href="/">Portada</a>              </li>
        <li>   <a href="/UnidadEducativa/">Mision_y_Vision</a>   </li>
        <li>   <a href="/Administrador/">Gestion Academica y Alumnos</a>     </li>
        <li>   <a href="/LOGIN/">Usuario y Contraseña</a>     </li>
        <li>   <a href="/Carga_de_documentos/">Datos personales</a>     </li>
    </ul>
"""


def Unidad_Educativa(request, plantilla="Unidad_Educativa.html"):
   return render(request, plantilla);


def UnidadEducativa(request, plantilla="UnidadEducativa.html"):
  return render(request, plantilla);


def Administrador(request, plantilla="Administrador.html"):
   return render(request, plantilla);


def Carga_de_documentos(request, plantilla="Carga_de_documentos.html"):
       return render(request, plantilla);


def LOGIN(request, plantilla="LOGIN.html"):
   return render(request, plantilla);

