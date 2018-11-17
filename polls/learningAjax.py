
class View(generic.ListView):
    template_name = 'polls/detail.html'
    #if want to change retrieved variable name,
    #context_object_name = 'question_list'

    def get_queryset(self):
        return Question.objects.order_by('-text')[:5]

# class ResultsView(generic.DetailView):
#     model = Question
#     template_name = 'polls/results.html'
    
    ##### MODELS

class Post(models.Model):
    author = models.ForeignKey(User)
    text = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.text+' - '+self.author.username

        #### view

def home(req):
    tmpl_vars = {
        'all_questions': Question.objects.reverse(),
        'form': QuestionForm()
    }
    return render(req, 'talk/index.html', tmpl_vars)

def likePost(request):
    if request.method == 'GET':
           post_id = request.GET['post_id']
           likedpost = Post.obejcts.get(pk=post_id) #getting the liked posts
           m = Like(post=likedpost) # Creating Like Object
           m.save()  # saving it to store in database
           return HttpResponse("Success!") # Sending an success response
    else:
           return HttpResponse("Request method is not a GET")
               
def create_post(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            return HttpResponseRedirect('/')
    else:
        form = QuestionForm()
    return render(request, 'post.html', {'form': form})

def create_post(request):
    if request.method == 'POST':
        post_text = request.POST.get('the_post')
        response_data = {}

        post = Post(text=post_text, author=request.user)
        post.save()

        response_data['result'] = 'Create post successful!'
        response_data['postpk'] = post.pk
        response_data['text'] = post.text
        response_data['created'] = post.created.strftime('%B %d, %Y %I:%M %p')
        response_data['author'] = post.author.username

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )