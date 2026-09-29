from django.shortcuts import render

def student_list(request):
    student = [
        {"name": "Jomar Jorquia", "age": 18, "course": "BSIT"},
        {"name": "Zedrick Lacuesta", "age": 19, "course": "BSA"},
        {"name": "Mark Anthony Llanora", "age": 20, "course": "BSE"},
        {"name": "Jhonas San Agustin", "age": 21, "course": "BSIT"},
        {"name": "Mark Vincent De Guzman", "age": 22, "course": "BSAIS"},
        {"name": "Rafael Metran", "age": 23, "course": "BSE"},
        {"name": "Neftaly Careg", "age": 24, "course": "BSA"},
        {"name": "Ceejay Petalvero", "age": 25, "course": "BSIT"},
        {"name": "Carl Chua", "age": 26, "course": "BSA"},
        {"name": "Geo Dalumpienes", "age": 27, "course": "BSE"}
    ]
    return render(request, "main/home.html", {"student": student})
