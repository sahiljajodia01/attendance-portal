from django.shortcuts import render, get_object_or_404
import os, csv


# Create your views here.

def index(request):
    return render(request, 'index.html')

def compsFE(request):
    return render(request, 'compsFE.html')

def compsSE(request):
    return render(request, 'compsSE.html')

def mechSE(request):
    return render(request, 'mechSE.html')


def excel_1(request):
    # if request.POST and request.FILES:
        # fout = open('uploaded_files/%s' % csvfile.name, 'wb')
        # fout.write(csvfile)

        # fout.close()
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        # ifile = open(os.path.join(BASE_DIR,'uploads','file1.csv'))
        # print(ifile)
    # with open(os.path.join(BASE_DIR,'uploads','file1.csv'),'w') as f:
    #
    #     reader = csv.reader(f)
    #     print(reader)
    #     for row in reader:
    #         print(row)


        # file = File.objects.get(pk=key)
    with open(os.path.join(BASE_DIR,'uploads','MathFEComps.csv'), newline='') as csvfile:
    #     with open(os.path.join(BASE_DIR, 'uploads', file), newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')

        # row = [row for row in spamreader]

            #return HttpResponse(response, row)
            # html = row
        # for row in spamreader:
        #     print(row[1])
        return render(request, "excel_1.html", {'file':spamreader})


