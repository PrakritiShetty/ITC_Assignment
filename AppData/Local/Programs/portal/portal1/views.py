from django.shortcuts import render
from .forms import user_form
from .models import portal1

FILE_TYPES=['pdf','jpg','jpeg','png','doc','docx']

def upload_bill(request):
    print(request)
    form=user_form()
    if request.method == 'POST':
        # form = ContactForm(request.POST)
        form= user_form(request.POST, request.FILES)
        # text=form.cleaned_data['user_pr']
        if form.is_valid():
            user_pr= form.save(commit=False)
            #text=form.cleaned_data['user_pr']
            #print(form.cleaned_data['user_pr'])
            user_pr.bill= request.FILES['bill']
            # text=form.cleaned_data['user_pr']
            file_type= user_pr.bill.url.split('.')[-1]
            file_type= file_type.lower()
            if file_type not in FILE_TYPES:
                return render( request, 'portal1/error.html')
            user_pr.save()
            
            return render(request,'portal1/details.html',{'user_pr':user_pr,})
    context={"form":form,}


    return render(request, 'portal1/create.html',context)

#     def store(request):
#         if request.method == "POST":
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#         return redirect('thankYou') # a second webpage where user should be redirected
# else:
#     form = ContactForm()
# return render(request, 'home/index.html', {'form': form})