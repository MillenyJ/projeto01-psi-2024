from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index.html")

def jogadores(request):
    jogadores = [
    {"nome": "Barbara", "idade": "36", 
     "posicao": "Goleiro", 
     "localdenascimento": "Recife,Pernambuco", 
     "foto": "jogadora9.jpg"},
    
    {"nome": "Duda Sampaio.", "idade": "23", 
     "posicao": "Atacante", 
     "localdenascimento": "Rio Casca,Minas Gerais", 
     "foto": "jogadora8.jpg"},
    
    {"nome": "Tamires", "idade": "37", 
     "posicao": "Defensor", 
     "localdenascimento": " Caeté, Minas Gerais", 
     "foto": "jogadora7.jpg"},
    
    {"nome": "Rafaelle", "idade": "33", 
     "posicao": "Defensor", 
     "localdenascimento": "Cipó, Bahia", 
     "foto": "jogadora6.jpg"},
    
    {"nome": "Adriana", "idade": "36", 
     "posicao": "Meio-campo", 
     "localdenascimento": "União, Piauí", 
     "foto": "jogadora5.jpg"},
    
    {"nome": "Kerolin", "idade": "24", 
     "posicao": "Atacante", 
     "localdenascimento": "Bauru, São paulo", 
     "foto": "jogadora4.jpg"},
    
    {"nome": "Debinha", "idade": "33", 
     "posicao": "Atacante", 
     "localdenascimento": "Brazópolis, Minas Gerais", 
     "foto": "jogadora3.jpg"},
    
    {"nome": "Beatriz", "idade": "30", 
     "posicao": "Atacante", 
     "localdenascimento": "Araraquara, São Paulo", 
     "foto": "jogadora2.jpg"},
    
    {"nome": "Antonia", "idade": "30", 
     "posicao": "Defensor", 
     "localdenascimento": "Pau dos Ferros, Rio Grande do Norte", 
     "foto": "jogadora1.jpg"},
    
    {"nome": "Gabriela Nunes", "idade": "27", 
     "posicao": "Atacante", 
     "localdenascimento": "São Paulo, São Paulo", 
     "foto": "jogadora11.jpg"},
    
    {"nome": "Monica", "idade": "37", 
     "posicao": "Meio-campo", 
     "localdenascimento": "Porto Alegre, Rio Grande do Sul", 
     "foto": "jogadora10.jpg"},

    ]

    context = {
        "jogadores": jogadores,
    }

    return render(request, "jogadores.html", context)

def sobre(request):
    return render(request, "sobre.html")