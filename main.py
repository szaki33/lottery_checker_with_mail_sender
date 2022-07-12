from urllib.request import urlopen
from mail import send_ej_numbers
from bs4 import BeautifulSoup

# url where we can find the numbers
url = "https://www.tipos.sk/loterie/eurojackpot"
# open url
html = urlopen(url)
# parse html
soup = BeautifulSoup(html, "html.parser")
# get numbers from html
x = soup.body.find('ul', attrs={'id': 'results'}).text
# here are our numbers
our_nums = [2, 9, 11, 30, 42, 2, 7]
nums = []
num = 0
length = 0
used_before = False


# function to check if we won the EJ
def check_if_we_won(lottery_numbers, our_numbers):
    hits = [0, 0]
    first = lottery_numbers[:5]
    second = lottery_numbers[5:]
    for i in range(0, 4):
        if our_numbers[i] in first:
            hits[0] += 1
    for i in range(0, 1):
        if our_numbers[i] in second:
            hits[1] += 1
    return hits


# for cykle to get numbers
for i in range(0, len(x)):
    num_s = ""
    length = length + 1
    if len(nums) == 5:
        nums = sorted(nums)
    if used_before is True:
        used_before = False
        continue
    else:
        try:
            num = int(x[i])
            num_s += x[i]
            try:
                num_s += x[length]
                num = int(num_s)
                used_before = True
            except ValueError:
                num = x[i]
            if len(nums) == 6:
                if num > nums[5]:
                    nums.append(num)
                else:
                    nums.insert(5, num)
            else:
                nums.append(num)
        except ValueError:
            continue

send_ej_numbers(nums, check_if_we_won(nums, our_nums))
