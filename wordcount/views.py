from django.shortcuts import render

def homepage(request):
    return render(request,'index.html')
def count(request):
    txt=request.GET['ftext']
    words=txt.split()
    dic={}
    for word in words:
        dic[word]=dic.get(word,0)+1
    sorted_list = sorted(dic.items(), key=lambda x:x[1], reverse=True)
    return render(request,'count.html',{'txt':txt,'words':len(words),'wordsdic':sorted_list})
def about(request):
    return render(request,'about.html')
