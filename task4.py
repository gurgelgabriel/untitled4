cookies_n = int(input("cookies number")) # ask the number of cookies you have
box_n = (cookies_n - cookies_n % 12)/12 # the formula to transform number of cookies in number of boxes
crates_n = (box_n - box_n % 20)/20 # the formula to transform the number of boxes in number of crates
value_cookies = cookies_n*0.5 # how much cookies worth individually
if 240 >= cookies_n >= 12: # in case you have from 12 to 240 cookies
    value_cookies = (cookies_n*0.416) + (cookies_n % 12) * (0.5) - (cookies_n % 12) * (0.416)  # how much cookies worth in case they have from 12 to 240 units
if cookies_n >= 240: # in case you have more than 240 cookies
    value_cookies = (cookies_n*0.33) + (cookies_n % 240) * (0.416) + (cookies_n % 12) * (0.5) - (cookies_n % 240) *(0.33) - (cookies_n % 12) * (0.33) # how much cookies worth in case you have more than 240


print(cookies_n)   # print how many cookies you have
print(box_n)       # print how many boxes you have
print(crates_n)    # print how many crates you have
print(value_cookies)  # print how much will the whole order cost

# OBS: cookies, boxes and crates are printed in integers and so if you have 250 cookies for example that is printed 1 crate and 10 cookies not as 1 crate and 250 cookies
