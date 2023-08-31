def handle_uploaded_file(f):
    with open("innika/static/property/"+f.name, "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)