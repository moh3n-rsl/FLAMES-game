RESULT = {'F':'Friends', 'L':'Love', 'A':'Affection', 'M':'Marriage', 'E':'Enemies', 'S':'Siblings'}
        
#####
def notCommonLettersCounts(str1, str2) -> int:

    for letter in min(str1, str2, key=len):
    
        if letter in max(str1, str2, key=len):
            str1 = str1.replace(letter, '', 1)
            str2 = str2.replace(letter, '', 1)

    return len(str1) + len(str2)
#####

#####
def startGame() -> None:
    # take names of players
    namePlayer1 = input('Enter player 1 name: ')
    namePlayer2 = input('Enter player 2 name: ')

    # count how many letter are not common in two names
    count = notCommonLettersCounts(namePlayer1, namePlayer2)

    flames = 'FLAMES'
    while True:
        index = 0

        # game ends when there is only one letter in flames variable
        if len(flames) == 1:
            break

        '''
            Example of how below codes work
            name1 = 'ali'
            name2 = 'alireza'

            here count is equal to 4 because "a" "l" "i" are common so we delete them once and count the other letters (it's reza)

            1. flames="FLAMES" -- remove M, then flames="ESFLA"
            2. flames="ESFLA"  -- remove L, then flames="AESF"
            3. flames="AESF"   -- remove F, then flames="AES"
            4. flames="AES"    -- remove A, then flames="ES"
            5. flames="ES"     -- remove S, then flames="E"

            now because (len(flames) == 1), the game ends
            and the result will be 'Enemy'

        '''
        for i in range(1, count+1):
            if i > len(flames):

                index = (i-len(flames))%len(flames) if i > 2*len(flames) else i - len(flames)
                
            else:
                index = i

        if count!=0: index-=1 

        flames = flames.replace(flames[index], '', 1)
        flames = flames[index:] + flames[:index]

    # game ends and print the result as output
    print('Relationship status :', RESULT.get(flames))
#####

startGame()