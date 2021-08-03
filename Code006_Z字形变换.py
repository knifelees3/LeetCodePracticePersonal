# %%
def convert(s: str, numRows: int) -> str:
    z_mat=[]
    len_s=len(s)
    for l in range(numRows):
        z_mat.append([])
    count_use=0
    count_full=0
    if numRows==1:
        return s
    else:
        while count_use<len_s:
            index_y=count_full%numRows
            index_x=int(count_full/numRows)
            count_full=count_full+1
            if index_x%(numRows-1)==0:
                z_mat[index_y].append(s[count_use])
                count_use=count_use+1
                print(count_use)
            if index_x%(numRows-1)>0 and index_x%(numRows-1)<numRows-1:
                if index_y==numRows-1-index_x%(numRows-1):
                    z_mat[index_y].append(s[count_use])
                    count_use=count_use+1
                    print(count_use)
                else:
                    z_mat[index_y].append(" ")
        for l in range(numRows):
            print(z_mat[l],'\n')
        new_mat=[]
        for l in range(numRows):
            for ele in z_mat[l]:
                if ele != ' ':
                    new_mat.append(ele)
        print("".join(new_mat))
        return "".join(new_mat)
convert('pdhoozufbkgswhmwruzpdfgysycpvmwlrfzfevkhitagaoctiejnlrodpqskeqxvwzccwpkekmkmapgltryeimjzeblirjfpkksgzeljqxvsmddhueleswdxxrhrapgmzasaeflwdippmuxiykpthssgjzzlqgxrisrnxelanaszxrjxdyqmtiteksqaapsljlahqljdodeluniamzmhhhltcduevopebpnrdzwrcaczqmzelnlvvwozakdvyvbakptpoqgqskrixqmkezfbwwaygfthauhnlcczsjsnvjvsakdgjkjhglfpqawrxfeijiietcrplmhnymvixepfpvwivuzsbfdlnnpjpgyaufotslbrqsyhpvpnpohrvkclxtumzsptzfmtqpkgkjqzefmvwumteqeejaskuheumsndkalulbtrhimfczyirdmdffnaotwbmlgyltsyvnpevclxdjiuowxudnwsgsvufdsrwkrtahzvjkvoudikbiefvaxduuyaxqtvdkpdtqacbvqxabhclohiqgllcjnzciwfulkockqfgjcimlkxztfqbsddeqeiybnsozgsjzzrkdawpmtqiaglujrabxibyxwpwejgfjxpmzlboguwiahfmafpyorylpnitxqzipoupcyfisbtukyildyjtrhhgxpzwhyewpanrasbstupguxtavevmncsktui',503)
# %%
a=[]
for l in range(4):
    a.append([])
print(a)
# %%
a[0].append(3)
print(a[0][0])
# %%
