# gpt2-tweeter

sess is the name of the default session.
gpt2.start_tf_sess() creates a new session, so if you want to run multiple models at the same time, you'll want to do that; just assign a var to that.
then it's gpt2.generate(session_name, temperature = 0.5, asList = False) to generate entries. (I think)
