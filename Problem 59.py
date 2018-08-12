def isEnglish(arr):
    english = True;
    for i in range(0,len(arr)):
        if (32 > arr[i] or 122 < arr[i] or (90 < arr[i] and 97 > arr[i])):
            english = False;
    return english;

file = open("p059_cipher.txt");
cipher = file.read().strip().split(",");
for x in range(0,len(cipher)):
    cipher[x] = int(cipher[x]);
cipherVals = [];
for x in range(0,len(cipher)):
    cipherVals.append(cipher[x]);
for a in range(97,123):
    for b in range(97,123):
        for c in range(97,123):
            for x in range(0,len(cipher)):
                cipherVals[x] = cipher[x];
            for x in range(0,len(cipherVals)):
                if(x%3==0):
                    cipherVals[x] = cipherVals[x] ^ a;
                elif(x%3==1):
                    cipherVals[x] = cipherVals[x] ^ b;
                else:
                    cipherVals[x] = cipherVals[x] ^ c;
            if(isEnglish(cipherVals)):
                answer = cipherVals;
                sum = 0;
                message = "";
                for i in range(0,len(answer)):
                    message += unichr(answer[i]);
                    sum += answer[i];
                print ("Message: " + message);
                print ("Key: " + unichr(a) + unichr(b) + unichr(c));
                print ("Ascii Sum: " + str(sum));