def main(args):
      name = args.get("name", "stranger")
      greeting = "Hello your majesty " + name + "!"
      print(greeting)
      return {"body": greeting}
  
