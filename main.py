from groq import Groq

client=Groq(api_key="YOUR_API_KEY")

conversation_history=[]             #this is the memory-->histry

conversation_history.append({'role':'system','content':"Acts as a president Donald Trump"})


while True:
    
    user_input=input("Type a message:")
    
   
    
    if user_input.lower()=='quit':
        break
    
    else:
        conversation_history.append({'role':'user',"content":user_input})

        response=client.chat.completions.create(
            
            model="llama-3.1-8b-instant",
            messages=conversation_history   #full history send to groq api
                
                # it's dictionary  which we are sendind to groq api
                # role-->> the user is us ,it's not the AI
                # content--->>> we are asking groq api, whoa are you?
            
            
        )
        

# print(response.choices[0].message.content)
    
    print(response.choices[0].message.content)   # AI reads everthing and replies
    
    AI_output=response.choices[0].message.content
    conversation_history.append({'role':'assistant','content':AI_output})          # this reply saves to history too
  