Hey bud, use the challenge_info script when you want to get all the challenge names and categorys for your site.

This way you only need to make one nice looking template and a python script should be able to create all the challenge pages 
through the template you make. 

I know this might take a little longer than doing it manually for now, but trust me. When we want to add more challenges 
in the future you a going to thank me.

to use my script... import it (duh) and currently there are two main utility_functions

challenge_info.get_challenge_settings(challenge_name), you put in the challenge name in question and it returns the settings 
for it, this is useful because we can store the answers here and change stuff all within one file.

and 

challenge_info.get_challanges(category_name), you use this to get all the challenges that are in the category. this will be useful
when you make your challenge pages so you can automatically add the challenges without manually typing them in.

I also wrote a temp.py file in this folder that you can run to see the syntax and output.

Hope this helps! :)

- Anthony