from unittest import result
from terminaltables import AsciiTable
import argparse

"""
The CKY parsing algorithm.

This file is part of the computer assignments for the course DD2418 Language engineering at KTH.
Created 2019 by Johan Boye.
"""

class CKY :

    # The unary rules as a dictionary from words to non-terminals,
    # e.g. { cuts : [Noun, Verb] }
    unary_rules = {}
    parents={}
    tree_str=str()

    # The binary rules as a dictionary of dictionaries. A rule
    # S->NP,VP would result in the structure:
    # { NP : {VP : [S]}} 
    binary_rules = {}

    # The parsing table
    table = []

    # The backpointers in the parsing table
    backptr = []

    # The words of the input sentence
    words = []


    # Reads the grammar file and initializes the 'unary_rules' and
    # 'binary_rules' dictionaries
    def __init__(self, grammar_file) :
        stream = open( grammar_file, mode='r', encoding='utf8' )
        for line in stream :
            rule = line.split("->")
            left = rule[0].strip()
            right = rule[1].split(',')
            if len(right) == 2 :
                # A binary rule
                first = right[0].strip()
                second = right[1].strip()
                if first in self.binary_rules :
                    first_rules = self.binary_rules[first]
                else :
                    first_rules = {}
                    self.binary_rules[first] = first_rules
                if second in first_rules :
                    second_rules = first_rules[second]
                    if left not in second_rules :
                        second_rules.append(left)
                else :
                    second_rules = [left]
                    first_rules[second] = second_rules
            if len(right) == 1 :
                # A unary rule
                word = right[0].strip()
                if word in self.unary_rules :
                    word_rules = self.unary_rules[word]
                    if left not in word_rules :
                        word_rules.append( left )
                else :
                    word_rules = [left]
                    self.unary_rules[word] = word_rules


    # Parses the sentence a and computes all the cells in the
    # parse table, and all the backpointers in the table
    def parse(self, s) :
        self.words = s.split()    
        # The parsing table table
        # The backpointers in the parsing table backptr
        # The unary rules as a dictionary from words to non-terminals,
        # e.g. { cuts : [Noun, Verb] }
        # unary_rules
        

       

        
        a = [[0]*len(self.words) for _ in range(len(self.words))]
        
        

        for i in range(0,len(self.words)):
            for j in range(i,-1,-1):
                
                if(i==j):
                    
                    a[i][j]=self.unary_rules.get(self.words[i])

                    rules=self.unary_rules.get(self.words[i])
                    
                    for r in rules:
                        self.parents[(r,i,j,0)]=(self.words[i])

                else:
                    x=i
                    while(x>j):
                        
                        if( a[x-1][j]!=0 and  a[i][x]!=0):
                            

                            if(self.check_match(a[x-1][j],a[i][x],i,j,x) is not None and self.check_match(a[x-1][j],a[i][x],i,j,x)!=0 ):
                            
                                a[i][j]=self.check_match(a[x-1][j],a[i][x],i,j,x)
                                
                            
                        x-=1
                


        temp=list()

        for j in range(0,len(self.words)):
            for i in range(0,len(self.words)):
                        if(a[i]==0):
                            temp.append([])
                        else:
                            temp.append(a[i][j])




                    
            self.table.append(temp)
            temp=[]

        

       




        
        
        
        

        #     
        #
        #  YOUR CODE HERE
        #
        pass


    def check_match(self,X,Y,I,J,Z):
        result=list()

        
        
        

        for i in X:
                
                
                if(self.binary_rules.get(i) is not None):
                    for j in Y:
                  
                        try:
                                    temp_d=self.binary_rules.get(i)
                                    
                                    
                                    
                                    temp_d=self.binary_rules.get(i)
                                    if(temp_d.get(j) is not None ):
                                        
                                        

                                        
                                        for K in range(0,10):
                                            

                                        
                
                                            if(self.parents.get(((temp_d.get(j))[0],I,J,K)) is not None and self.parents.get(((temp_d.get(j))[0],I,J,K))!=0 and self.parents.get(((temp_d.get(j))[0],I,J,K))!=[]):
                                                K+=1
                                                break;
                                            break;
                                        

                                        for g in range(0,len((temp_d.get(j)))):
                                            
                                            self.parents[((temp_d.get(j))[g],I,J,K)]=[(i,Z-1,J,0),(j,I,Z,0)]
                                            result.append((temp_d.get(j))[g])
                                        
                            
                                        
                        except:
                                
                                
                                return
        

        

        

        if(len(result)==0):
            return 0

        return result
        


    # Prints the parse table
    def print_table( self ) :
        t = AsciiTable(self.table)
        t.inner_heading_row_border = False
        print( t.table )

    def print_trees(self,row,column,symbol):
        
        (self.print_trees_nm(symbol,row,column))
        print(self.tree_str)
        
        


    def  print_trees_nm(self, symbol,column,row):
        
        

        for i in range(0,10):
            
            if(self.parents.get((symbol,column,row,i)) is not None):
                
                self.multiple_path_check(symbol,column,row,i)
                print('here',symbol,column,row,i)
                self.tree_str=self.tree_str+'   '
                i+=1
                
            else:
                break 
        




    # Prints all parse trees derivable from cell in row 'row' and
    # column 'column', rooted with the symbol 'symbol'
    def multiple_path_check( self, symbol,column,row,fl ) :
        #
        #  YOUR CODE HERE
        #
        if (type (self.parents.get((symbol,column,row,fl))) is str):
            
            
            self.tree_str=self.tree_str+symbol+'('
            
            self.tree_str=self.tree_str+self.parents.get((symbol,column,row,fl))+'),'
            return


        
        

        
        (X,Y)=self.parents.get((symbol,column,row,fl))
        

        
        (I,J,K,L)=X
        
        

        
        
        self.tree_str=self.tree_str+symbol+'('
        
        
        self.multiple_path_check(I,J,K,L)
        
        
        

        
        (I,J,K,L)=Y
        self.multiple_path_check(I,J,K,L)
        
        self.tree_str=self.tree_str+')'

       



        pass


def main() :

    # Parse command line arguments
    parser = argparse.ArgumentParser(description='CKY parser')
    parser.add_argument('--grammar', '-g', type=str,  required=True, help='The grammar describing legal sentences.')
    parser.add_argument('--input_sentence', '-i', type=str, required=True, help='The sentence to be parsed.')
    parser.add_argument('--print_parsetable', '-pp', action='store_true', help='Print parsetable')
    parser.add_argument('--print_trees', '-pt', action='store_true', help='Print trees')
    parser.add_argument('--symbol', '-s', type=str, default='S', help='Root symbol')

    arguments = parser.parse_args()

    cky = CKY( arguments.grammar )
    cky.parse( arguments.input_sentence )
    if arguments.print_parsetable :
        cky.print_table()
    if arguments.print_trees :
        
        
        cky.print_trees( len(cky.words)-1, 0, 'S' )
    

if __name__ == '__main__' :
    main()    


                        
                        
                        
                    
                
                    

                
        
    
