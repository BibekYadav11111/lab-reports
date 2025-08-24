def student_profile(**args):
    for key,value in args.items():
        print(f'{key} : {value}')
student_profile(name='bandhan',age=10)