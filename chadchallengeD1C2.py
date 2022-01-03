                                                                                                                                                                                                                                                            
#!/usr/bin/env python3
import datetime
day = datetime.date(2020,7,24).strftime('%A')
name = input("Please enter your usernames: ")
## the line below creates a single string that is passed to print()
print("Hello, " + name + "Happy " + day + "!")

