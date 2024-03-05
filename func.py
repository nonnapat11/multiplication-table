def ascii_art():
  return print('''\
               
█▀▄▀█ ▄▀█ █▀▄ █▀▀   █▄▄ █▄█   █▀▄ █░░
█░▀░█ █▀█ █▄▀ ██▄   █▄█ ░█░   █▄▀ █▄▄
               
         ''')


def trable_all(trable, trable_last, trable_block):
    if trable < trable_last:
         for i in range(trable, trable_last+1):
              if i != trable_block:
                print()  
                print(f'สูตรคูณแม่{i}')
                for x in range(1, 13):
                    print(f'{i} x {x} = {i*x}')
    else:
         for i in range(trable, trable_last-1,-1):
              if i != trable_block:
                print()  
                print(f'สูตรคูณแม่{i}')
                for x in range(1, 13):
                    print(f'{i} x {x} = {i*x}')