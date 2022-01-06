#!/usr/bin/env python3

challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]


trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]


nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

print("challenge level -----------------------------------------------")

a= challenge[2][1]
b= challenge[2][0]
c= challenge[-1]

print(f"My {a}! The {b} do {c}!")

print("Trial level---------------------------------------------------")

d= trial[2]["goggles"]
e= trial[2]["eyes"]
f= trial[-1]
print(f"My {d}! The {e} do {f}!")

print("Nightmare level---------------------------------------------------")

g= nightmare[0]["user"]["name"]["first"]
h= nightmare[0]["kumquat"]
i= nightmare[0]["d"]

print(f"My {g}! The {h} do {i}!")

