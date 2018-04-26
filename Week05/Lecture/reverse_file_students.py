from array_stack_Students import ArrayStack


def reverse_file(filename):
    """Overwrite given file with its contents line-by-line reversed."""
    inputFile = open("DSSyllabus.txt", 'r')
    myStack = ArrayStack()
    for i in inputFile:
        myStack.push(i)
    inputFile.close()

    # now we overwrite with contents in LIFO order
    output = open("DSSyllabus.txt", 'w')  # reopening file overwrites original
    while not myStack.isEmpty():
        output.write(myStack.pop())
    output.close()


reverse_file('DSSyllabus.txt')
