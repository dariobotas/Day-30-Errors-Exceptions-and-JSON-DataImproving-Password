

def main():
  #FileNotFound
  #with open("a_file.txt") as file:
  #  file.read()

  #KeyError
  #a_dictionary = {"key": "value"}
  #value = a_dictionary["non_existent_key"]

  #IndexError
  #a_list = ["a", "b", "c"]
  #value = a_list[3]

  #TypeError
  #a_string = "a string"
  #value = a_string.upper()
  #print(a_string + 5)

  #ZeroDivisionError
  #1 / 0

  #NameError
  #value = non_existent_variable

  #AttributeError
  #a_list = ["a", "b", "c"]
  #value = a_list.append("d")

  #RuntimeError
  #raise RuntimeError("An error occurred")

  #SyntaxError
  #a_list = ["a", "b", "c"]
  #value = a_list.append("d")

  #try: - Something that might cause an exception
  #except: Do this if there was an exception
  #else: Do this if there were no exceptions
  #finally: Do ths no matter what happens

  try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["sdsa"])
  #except:
    #print("An error occurred")
    #file = open("a_file.txt", "w")
    #file.write("Hello World")
  except FileNotFoundError:
    print("File not found")
  except PermissionError:
    print("Permission denied")
  except KeyError as error_message:
    print(f"The key {error_message} does not exist")
  else:
    content = file.read()
    print("File opened")
    print(content)
  finally:
    file.close()
    print("File was closed.")