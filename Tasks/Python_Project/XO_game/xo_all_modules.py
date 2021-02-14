import random
from IPython.display import clear_output
class XO_game:
    def __init__(self,game_mode):
        self.game_mode=game_mode
        self.player_one_sign=[]
        self.player_two_sign=[]
        self.whose_win=''
        self.dash_board=['0','0','0','0','0','0','0','0','0']
        self.wins_position=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
        self.whose_next='X' 
        self.type_of_player1=''
        self.type_of_player2=''
        
    def create_game_Mode(self):
        if self.game_mode=='TwoPlayer':
            self.type_of_player1=input('please enter player one name')
            self.type_of_player2=input('please enter player two name')
        if self.game_mode=='HumanToComputer':
            self.type_of_player1=input('please enter player one name')
            self.type_of_player2='Computer_random'
        if self.game_mode=='HumanToIntelligentComp':
            self.type_of_player1=input('please enter player one name')
            self.type_of_player2='IntelligentComputer'
        if self.game_mode=='IntelligentCompToIntelligentComp':
            self.type_of_player1='IntelligentComp1'
            self.type_of_player2='IntelligentComp2'
    
    def set_sign_player1(self):
        pass
    def set_sign_player2(self):
        pass
    def check_player_win(self):
        pass
    
    def draw_dash_board(self):
        print('--------')
        count=1
        for item in self.dash_board:
            if count % 3==0:
                print (f'{item} ')
                print('--------')
            else:
                print (f'{item} |',end="")
                
            count=count+1
    
    def start_play(self):
        print('start')
        count_of_play=0
        self.draw_dash_board()
        while self.dash_board.count('0')!=0 and self.whose_win=='' and count_of_play<50:
            if self.whose_next =='X':
                print(f'player: {self.type_of_player1}')
                self.set_sign_player1()
                self.whose_next='O'
            else:
                print(f'player: {self.type_of_player2}')
                self.set_sign_player2()
                self.whose_next='X'
            count_of_play=count_of_play+1
            ##input('Next>>>>>')
            if self.whose_win=='':
                clear_output(wait=True)
                self.draw_dash_board()
            
            
        clear_output(wait=True)
        self.draw_dash_board()
        if self.whose_win=='':
            print('no winner')
            return
        print(f'WOW ,,,, winner is {self.whose_win}')
            
            
###############################################################################################################################
#################################################player one####################################################################
###############################################################################################################################

class XO_game_intell_comp_to_intell_comp(XO_game):
    def __init__(self,game_mode):
        XO_game.__init__(self,game_mode)           
        
    def set_sign_player1(self):
        index_to_play=len(self.player_one_sign)
        is_go_to_win=False
        if index_to_play==2:
            for item in self.wins_position:
                if(item[0:3:2]==self.player_one_sign or item[0:3:2]==self.player_one_sign[-1:-3:-1] )  and self.dash_board[item[1]]=='0':
                    self.player_one_sign.append(item[1])
                    self.dash_board[item[1]]='X'
                    is_go_to_win=True
                    self.whose_win=self.type_of_player1
                    print('x win')
                    return
                if (item[0:2:1]==self.player_one_sign or item[0:2:1]==self.player_one_sign[-1:-3:-1] )  and self.dash_board[item[2]]=='0':
                    self.player_one_sign.append(item[2])
                    self.dash_board[item[2]]='X'
                    is_go_to_win=True
                    self.whose_win=self.type_of_player1
                    print('x win')
                    return
                if (item[1:3:1]==self.player_one_sign or item[1:3:1]==self.player_one_sign[-1:-3:-1] )  and self.dash_board[item[0]]=='0':
                    self.player_one_sign.append(item[0])
                    self.dash_board[item[0]]='X'
                    is_go_to_win=True
                    self.whose_win=self.type_of_player1
                    print('x win')
                    return
        if index_to_play==3:
            for item in self.wins_position:
                if self.player_one_sign==item or self.player_one_sign==item[-1:-4:-1] :
                    is_go_to_win=True
                    self.whose_win=self.type_of_player1
                    print('x win')
                    return;
            for item in self.wins_position:
                ##print('item[0:3:2]==self.player_one_sign[0:3:2] or item[0:3:2]==self.player_one_sign[-1:-4:-2] )  and self.dash_board[item[1:2]]==0')
                ##print(f'item[0:3:2] is {item[0:3:2]} and self.player_one_sign[0:3:2] = {self.player_one_sign[0:3:2]}or and self.player_one_sign[-1:-4:-2]= {self.player_one_sign[-1:-4:-2]} ) and self.dash_board[item[1:2]]={self.dash_board[item[1]]} ')
                ##[0:3:2]
                if (item[0:3:2]==self.player_one_sign[0:3:2] or item[0:3:2]==self.player_one_sign[-1:-4:-2] )  and self.dash_board[item[1]]=='0':
                    index_which_will_move=self.player_one_sign[1]
                    self.dash_board[index_which_will_move]='0'
                    self.player_one_sign[1]=item[1]
                    self.dash_board[item[1]]='X'
                    is_go_to_win=True
                    self.whose_win=self.type_of_player1
                    print('x win')
                    return
                if (item[0:2:1]==self.player_one_sign[0:3:2] or item[0:2:1]==self.player_one_sign[-1:-4:-2] )  and self.dash_board[item[2]]=='0':
                    index_which_will_move=self.player_one_sign[1]
                    self.dash_board[index_which_will_move]='0'
                    self.player_one_sign[1]=item[2]
                    self.dash_board[item[2]]='X'
                    is_go_to_win=True
                    self.whose_win=self.type_of_Player1
                    print(' x win')
                    return
                if (item[1:3:1]==self.player_one_sign[0:3:2] or item[1:3:1]==self.player_one_sign[-1:-4:-2] )  and self.dash_board[item[0]]=='0':
                    index_which_will_move=self.player_one_sign[1]
                    self.dash_board[index_which_will_move]='0'
                    self.player_one_sign[1]=item[0]
                    self.dash_board[item[0]]='X'
                    is_go_to_win=True
                    self.whose_win=self.type_of_player1
                    print('x win')
                    return
                       
                    
                ##print('item[0:2:1]==self.player_one_sign[0:2:1] or item[0:2:1]==self.player_one_sign[-2:-4:-1] )  and self.dash_board[item[2]]==0')
                ##print(f'item[0:2:1]= {item[0:2:1]} and self.player_one_sign[0:2:1] ={self.player_one_sign[0:2:1]}  and  self.player_one_sign[-2:-4:-1] ={self.player_one_sign[-2:-4:-1]} and self.dash_board[item[2]]={self.dash_board[item[2]]}')
                ##[0:2:1]
                if (item[0:2:1]==self.player_one_sign[0:2:1] or item[0:2:1]==self.player_one_sign[-2:-4:-1])and self.dash_board[item[2]]=='0':
                    index_which_will_move=self.player_one_sign[2]
                    self.dash_board[index_which_will_move]='0'
                    self.player_one_sign[2]=item[2]
                    self.dash_board[item[2]]='X'
                    is_go_to_win=True
                    self.whose_win=self.type_of_player1
                    print('x win')
                    return
                if (item[0:3:2]==self.player_one_sign[0:2:1] or item[0:3:2]==self.player_one_sign[-2:-4:-1])and self.dash_board[item[1]]=='0':
                    index_which_will_move=self.player_one_sign[2]
                    self.dash_board[index_which_will_move]='0'
                    self.player_one_sign[2]=item[1]
                    self.dash_board[item[1]]='X'
                    is_go_to_win=True
                    self.whose_win=self.type_of_player1
                    print('x win')
                    return
                if (item[1:3:1]==self.player_one_sign[0:2:1] or item[1:3:1]==self.player_one_sign[-2:-4:-1])and self.dash_board[item[0]]=='0':
                    index_which_will_move=self.player_one_sign[2]
                    self.dash_board[index_which_will_move]='0'
                    self.player_one_sign[2]=item[0]
                    self.dash_board[item[0]]='X'
                    is_go_to_win=True
                    self.whose_win=self.type_of_player1
                    print('x win')
                    return
                ##print(f'item[1:3:1]= {item[1:3:1]} and self.player_one_sign[1:3:1] ={self.player_one_sign[1:3:1]}  and  self.player_one_sign[-1:-3:-1] ={self.player_one_sign[-1:-3:-1]} and self.dash_board[item[0]]={self.dash_board[item[0]]}')
                ##[1:3:1]
                if (item[1:3:1]==self.player_one_sign[1:3:1] or item[1:3:1]==self.player_one_sign[-1:-3:-1] )  and self.dash_board[item[0]]=='0':
                    index_which_will_move=self.player_one_sign[0]
                    self.dash_board[index_which_will_move]='0'
                    self.player_one_sign[0]=item[0]
                    self.dash_board[item[0]]='X'
                    is_go_to_win=True
                    self.whose_win=self.type_of_player1
                    print('x win')
                    return
                if (item[0:2:1]==self.player_one_sign[1:3:1] or item[0:2:1]==self.player_one_sign[-1:-3:-1] )  and self.dash_board[item[2]]=='0':
                    index_which_will_move=self.player_one_sign[0]
                    self.dash_board[index_which_will_move]='0'
                    self.player_one_sign[0]=item[2]
                    self.dash_board[item[2]]='X'
                    is_go_to_win=True
                    self.whose_win=self.type_of_player1
                    print('x win')
                    return
                if (item[0:3:2]==self.player_one_sign[1:3:1] or item[0:3:2]==self.player_one_sign[-1:-3:-1] )  and self.dash_board[item[1]]=='0':
                    index_which_will_move=self.player_one_sign[0]
                    self.dash_board[index_which_will_move]='0'
                    self.player_one_sign[0]=item[1]
                    self.dash_board[item[1]]='X'
                    is_go_to_win=True
                    self.whose_win=self.type_of_player1
                    print('x win')
                    return
                    
       
                
                       
        ##Take care check first can other player win
        ##can other player win
        index=self.can_other_player_win(self.player_two_sign,self.dash_board)
        if index!=-1:
            self.dash_board[index]='X'
            if len(self.player_one_sign)<3:
                self.player_one_sign.append(index)
                return
            else:
                index_move=self.is_player_safe_to_move(self.player_one_sign,self.player_two_sign)
                self.player_one_sign[self.player_one_sign.index(index_move)]=index
                self.dash_board[index_move]='0'
                return           
      
            
        ##May be win next time
        if is_go_to_win==False:
            index=0
            if len(self.player_one_sign)<=2:
                index_initial_list=[]
                index_list_count=0
                for i in self.dash_board:
                    if i=='0':
                        index_initial_list.append(index_list_count)
                    index_list_count=index_list_count+1
                index_initial=random.choice(index_initial_list)
                self.player_one_sign.append(index_initial)
                self.dash_board[index_initial]='X'
                return
            
            
            ##if len ==2 or len==3
            len2_index=0
            '''if (len(self.player_one_sign)==2 or len(self.player_two_sign)==2) and self.dash_board[4]=='0':
                print('aliiiiiiiiiiii')
                self.player_one_sign.append(4)
                self.dash_board[4]='X'
                return
                '''
            for item in self.dash_board:
                if item=='0':
                    if len(self.player_one_sign)==3:
                        move=self.is_player_safe_to_move(self.player_one_sign,self.player_two_sign)
                        self.dash_board[move]='0'
                        self.player_one_sign[self.player_one_sign.index(move)]=len2_index
                        self.dash_board[len2_index]='X'
                        return
                    self.dash_board[len2_index]='X'
                    self.player_one_sign.append(len2_index)
                    break;
                len2_index=len2_index+1
            
            

    
                    
                        
            
###############################################################################################################################
#################################################player two####################################################################
###############################################################################################################################

    def set_sign_player2(self):
       
        ##check if can I win
        
        index_to_play=len(self.player_two_sign)
        is_go_to_win=False
        if index_to_play==2:
            for item in self.wins_position:
                if (item[0:3:2]==self.player_two_sign or item[0:3:2]==self.player_two_sign[-1:-3:-1] )  and self.dash_board[item[1]]=='0':
                    self.player_two_sign.append(item[1])
                    self.dash_board[item[1]]='O'
                    is_go_to_win=True
                    self.whose_win=self.type_of_player2
                    print('y win')
                    return
                if (item[0:2:1]==self.player_two_sign or item[0:2:1]==self.player_two_sign[-1:-3:-1] )  and self.dash_board[item[2]]=='0':
                    self.player_two_sign.append(item[2])
                    self.dash_board[item[2]]='O'
                    is_go_to_win=True
                    self.whose_win=self.type_of_player2
                    print('y win')
                    return
                if (item[1:3:1]==self.player_two_sign or item[1:3:1]==self.player_two_sign[-1:-3:-1] )  and self.dash_board[item[0]]=='0':
                    self.player_two_sign.append(item[0])
                    self.dash_board[item[0]]='O'
                    is_go_to_win=True
                    self.whose_win=self.type_of_player2
                    print('y win')
                    return
                    
        if index_to_play==3:
            for item in self.wins_position:
                if self.player_two_sign==item or self.player_two_sign==item[-1:-4:-1] :
                    is_go_to_win=True
                    self.whose_win=self.type_of_player2
                    print('y win')
                    return;
                    
            for item in self.wins_position:
                ##[0:3:2]
                if (item[0:3:2]==self.player_two_sign[0:3:2] or item[0:3:2]==self.player_two_sign[-1:-4:-2] )  and self.dash_board[item[1]]=='0':
                    index_which_will_move=self.player_two_sign[1]
                    self.dash_board[index_which_will_move]='0'
                    self.player_two_sign[1]=item[1]
                    self.dash_board[item[1]]='O'
                    is_go_to_win=True
                    self.whose_win=self.type_of_player2
                    print('y win')
                    return
                if (item[0:2:1]==self.player_two_sign[0:3:2] or item[0:2:1]==self.player_two_sign[-1:-4:-2] )  and self.dash_board[item[2]]=='0':
                    index_which_will_move=self.player_two_sign[1]
                    self.dash_board[index_which_will_move]='0'
                    self.player_two_sign[1]=item[2]
                    self.dash_board[item[2]]='O'
                    is_go_to_win=True
                    self.whose_win=self.type_of_player2
                    return
                if (item[1:3:1]==self.player_two_sign[0:3:2] or item[0:2:1]==self.player_two_sign[-1:-4:-2] )  and self.dash_board[item[0]]=='0':
                    index_which_will_move=self.player_two_sign[1]
                    self.dash_board[index_which_will_move]='0'
                    self.player_two_sign[1]=item[0]
                    self.dash_board[item[0]]='O'
                    is_go_to_win=True
                    self.whose_win=self.type_of_player2
                    print('y win')
                    return
                ##[0:2:1]    
                if (item[1:3:1]==self.player_two_sign[0:2:1] or item[1:3:1]==self.player_two_sign[-2:-4:-1] )  and self.dash_board[item[0]]=='0':
                    index_which_will_move=self.player_two_sign[2]
                    self.dash_board[index_which_will_move]='0'
                    self.player_one_sign[2]=item[0]
                    self.dash_board[item[0]]='O'
                    is_go_to_win=True
                    self.whose_win=self.type_of_player2
                    print('y win')
                    return
                if (item[0:2:1]==self.player_two_sign[0:2:1] or item[0:2:1]==self.player_two_sign[-2:-4:-1] )  and self.dash_board[item[2]]=='0':
                    index_which_will_move=self.player_two_sign[2]
                    self.dash_board[index_which_will_move]='0'
                    self.player_one_sign[2]=item[2]
                    self.dash_board[item[2]]='O'
                    is_go_to_win=True
                    self.whose_win=self.type_of_player2
                    print('y win')
                    return
                if (item[0:3:2]==self.player_two_sign[0:2:1] or item[0:3:2]==self.player_two_sign[-2:-4:-1] )  and self.dash_board[item[1]]=='0':
                    index_which_will_move=self.player_two_sign[2]
                    self.dash_board[index_which_will_move]='0'
                    self.player_one_sign[2]=item[1]
                    self.dash_board[item[1]]='O'
                    is_go_to_win=True
                    self.whose_win=self.type_of_player2
                    print('y win')
                    return
                ##[1:3:1]
                if (item[1:3:1]==self.player_two_sign[1:3:1] or item[1:3:1]==self.player_two_sign[-1:-3:-1] )  and self.dash_board[item[0]]=='0':
                    index_which_will_move=self.player_two_sign[0]
                    self.dash_board[index_which_will_move]='0'
                    self.player_two_sign[0]=item[0]
                    self.dash_board[item[0]]='O'
                    is_go_to_win=True
                    self.whose_win=self.type_of_player2
                    print('y win')
                    return
                if (item[0:2:1]==self.player_two_sign[1:3:1] or item[0:2:1]==self.player_two_sign[-1:-3:-1] )  and self.dash_board[item[2]]=='0':
                    index_which_will_move=self.player_two_sign[0]
                    self.dash_board[index_which_will_move]='0'
                    self.player_two_sign[0]=item[2]
                    self.dash_board[item[2]]='O'
                    is_go_to_win=True
                    self.whose_win=self.type_of_player2
                    print('y win')
                    return
                if (item[0:3:2]==self.player_two_sign[1:3:1] or item[0:3:2]==self.player_two_sign[-1:-3:-1] )  and self.dash_board[item[1]]=='0':
                    index_which_will_move=self.player_two_sign[0]
                    self.dash_board[index_which_will_move]='0'
                    self.player_two_sign[0]=item[1]
                    self.dash_board[item[1]]='O'
                    is_go_to_win=True
                    self.whose_win=self.type_of_player2
                    print('y win')
                    return
                    
## defend on my self : check other player can win
        
        index=self.can_other_player_win(self.player_one_sign,self.dash_board)
        ##print(index)
        if index!=-1:
            self.dash_board[index]='O'
            if len(self.player_two_sign)<3:
                self.player_two_sign.append(index)
                return
            
            else:
                index_move=self.is_player_safe_to_move(self.player_two_sign,self.player_one_sign)
                self.player_two_sign[self.player_two_sign.index(index_move)]=index
                self.dash_board[index_move]='0'
                return                          
        
##May be win next time

        if is_go_to_win==False:
            index=0
            if len(self.player_one_sign)<=2:
                index_initial_list=[]
                index_list_count=0
                for i in self.dash_board:
                    if i=='0':
                        index_initial_list.append(index_list_count)
                    index_list_count=index_list_count+1
                index_initial=random.choice(index_initial_list)
                self.player_two_sign.append(index_initial)
                self.dash_board[index_initial]='O'
                return
            
            len2_index=0
            '''if (len(self.player_two_sign)==2 or len(self.player_one_sign)==2) and self.dash_board[4]=='0':
                print('aliiiiiiiiiiii')
                self.player_two_sign.append(4)
                self.dash_board[4]='O'
                return'''
                
            for item in self.dash_board:
                if item=='0':
                    if len(self.player_two_sign)==3:
                        move=self.is_player_safe_to_move(self.player_two_sign,self.player_one_sign)
                        self.dash_board[move]='0'
                        self.player_two_sign[self.player_two_sign.index(move)]=len2_index
                        self.dash_board[len2_index]='O'
                        return
                    self.dash_board[len2_index]='O'
                    self.player_two_sign.append(len2_index)
                    break;
                len2_index=len2_index+1
                
        
##support method#####################################################################################    
        
            
    def is_player_safe_to_move(self,list_to_check,other_player):
       
        default=list_to_check[0]
        for item in list_to_check:
            new_dash_board=[i for i in self.dash_board]
            new_dash_board[item]='0'
            if self.can_other_player_win(other_player,new_dash_board)==-1:
                return item
            
        return default
    
              
     
            
                       
        
    def can_other_player_win(self,data,new_dash_board):
        index_to_play=len(data)
        is_go_to_win=False
        if index_to_play==2:
            for item in self.wins_position:
                if (item[0:3:2]==data or item[0:3:2]==data[-1:-3:-1] )  and new_dash_board[item[1]]=='0':
                    return item[1]
                if (item[0:2:1]==data or item[0:2:1]==data[-1:-3:-1] )  and new_dash_board[item[2]]=='0':
                    return item[2]                  
                if (item[1:3:1]==data or item[1:3:1]==data[-1:-3:-1] )  and new_dash_board[item[0]]=='0':
                    return item[0]
                    
        if index_to_play==3:        
            for item in self.wins_position:
                ##[0:3:2]
                if (item[0:3:2]==data[0:3:2] or item[0:3:2]==data[-1:-4:-2] )  and new_dash_board[item[1]]=='0':
                    return item[1]
                if (item[0:2:1]==data[0:3:2] or item[0:2:1]==data[-1:-4:-2] )  and new_dash_board[item[2]]=='0':
                    return item[2]
                if (item[1:3:1]==data[0:3:2] or item[0:2:1]==data[-1:-4:-2] )  and new_dash_board[item[0]]=='0':
                    return item[0]
                ##[0:2:1]    
                if (item[1:3:1]==data[0:2:1] or item[1:3:1]==data[-2:-4:-1] )  and new_dash_board[item[0]]=='0':
                    return item[0]
                if (item[0:2:1]==data[0:2:1] or item[0:2:1]==data[-2:-4:-1] )  and new_dash_board[item[2]]=='0':
                    return item[2]
                if (item[0:3:2]==data[0:2:1] or item[0:3:2]==data[-2:-4:-1] )  and new_dash_board[item[1]]=='0':
                    return item[1]
                ##[1:3:1]
                if (item[1:3:1]==data[1:3:1] or item[1:3:1]==data[-1:-3:-1] )  and new_dash_board[item[0]]=='0':
                    return item[0]
                if (item[0:2:1]==data[1:3:1] or item[0:2:1]==data[-1:-3:-1] )  and new_dash_board[item[2]]=='0':
                    return item[2]
                if (item[0:3:2]==data[1:3:1] or item[0:3:2]==data[-1:-3:-1] )  and new_dash_board[item[1]]=='0':
                    return item[1]
        return -1
    
    def start_play(self):
        print('start')
        count_of_play=0
        self.draw_dash_board()
        while self.dash_board.count('0')!=0 and self.whose_win=='' and count_of_play<50:
            if self.whose_next =='X':
                print(f'player: {self.type_of_player1}')
                self.set_sign_player1()
                self.whose_next='O'
            else:
                print(f'player: {self.type_of_player2}')
                self.set_sign_player2()
                self.whose_next='X'
            count_of_play=count_of_play+1
            input('Next>>>>>')
            if self.whose_win=='':
                clear_output(wait=True)
                self.draw_dash_board()
            
            
        clear_output(wait=True)
        self.draw_dash_board()
        if self.whose_win=='':
            print('no winner')
            return
        print(f'WOW ,,,, winner is {self.whose_win}')
    

            
class  XO_game_human_with_human(XO_game):
    def __init__(self,game_mode):
        XO_game.__init__(self,game_mode)
    
    def set_sign_player1(self):
        another_position=True
        while(another_position):
            try:
                position_from=-1
                position_to=-1
                print(self.player_one_sign)
                if len(self.player_one_sign)==3:
                    print('ali')
                    position_from=int(input('please choice your position to play from:'))
                    position_to=int(input('please choice your position to play to:'))
                    if (position_from > 8 or position_from <0)or(position_to > 8 or position_to <0):
                        print('wrong position range')
                        another_position=True
                    else:
                        another_position=False
                        if self.dash_board[position_to]=='0':
                            self.dash_board[position_to]='X'
                            self.dash_board[position_from]='0'
                            self.player_one_sign[self.player_one_sign.index(position_from)]=position_to
                            self.player_one_sign.sort()
                            if self.check_player_win(self.player_one_sign):
                                self.whose_win=self.type_of_player1
                                
                            return
                        else:
                            print('can not move wrong position, select another')
                            another_position=True
                            
                else:
                    position_to=int(input('please choice your position to play to:'))
                    if position_to > 8 and position_to <0:
                        print('wrong position range')
                        another_position=True
                    else:
                        another_position=False
                        if self.dash_board[position_to]=='0':
                            self.dash_board[position_to]='X'
                            self.player_one_sign.append(position_to)
                            self.player_one_sign.sort()
                            if len(self.player_one_sign)==3:
                                if self.check_player_win(self.player_one_sign):
                                    self.whose_win=self.type_of_player1
                            return
                        else:
                            print('can not move wrong position, select another')
                            another_position=True
                
                
                
                        
                    
            except Exception as e:
                print(type(e).__name__)
    
    
    def set_sign_player2(self):
        another_position=True
        while(another_position):
            try:
                print('Aly')
                position_from=-1
                position_to=-1
                if len(self.player_two_sign)==3:
                    position_from=int(input('please choice your position to play from:'))
                    position_to=int(input('please choice your position to play to:'))
                    if (position_from >8 or position_from <0)or(position_to >8  or position_to <0):
                        print('wrong position range')
                        another_position=True
                    else:
                        another_position=False
                        if self.dash_board[position_to]=='0':
                            self.dash_board[position_to]='O'
                            self.dash_board[position_from]='0'
                            self.player_two_sign[self.player_two_sign.index(position_from)]=position_to
                            self.player_two_sign.sort()
                            if self.check_player_win(self.player_two_sign):
                                self.whose_win=self.type_of_player2
                            return
                        else:
                            print('can not move wrong position, select another')
                            another_position=True
                            
                else:
                    position_to=int(input('please choice your position to play to:'))
                    if position_to >8 and position_to <0:
                        print('wrong position range')
                        another_position=True
                    else:
                        another_position=False
                        if self.dash_board[position_to]=='0':
                            self.dash_board[position_to]='O'
                            self.player_two_sign.append(position_to)
                            self.player_two_sign.sort()
                            if len(self.player_two_sign)==3:
                                if self.check_player_win(self.player_two_sign):
                                    self.whose_win=self.type_of_player2
                            return
                        
                        else: 
                            print('can not move wrong position, select another')
                            another_position=True
                    
            except Exception as e:
                print(type(e).__name__)
    
    
    
    def check_player_win(self,data):
        for item in self.wins_position:
            item.sort()
            if item==data :
                return True
        return False

    
    
    
class  XO_game_human_with_computer_random(XO_game_human_with_human):
    def __init__(self,game_mode):
        XO_game_human_with_human.__init__(self,game_mode)
    def set_sign_player2(self):
        try:
            position_from=-1
            position_to=-1
            if len(self.player_two_sign)==3:
                position_from=random.choice(self.player_two_sign)
                position_to=self.random_position_to()                   
                if self.dash_board[position_to]=='0':
                    self.dash_board[position_to]='O'
                    self.dash_board[position_from]='0'
                    self.player_two_sign[self.player_two_sign.index(position_from)]=position_to
                    self.player_two_sign.sort()
                    if self.check_player_win(self.player_two_sign):
                        self.whose_win=self.type_of_player2
                        return


            else:
                index_initial=self.random_position_to()
                self.player_two_sign.append(index_initial)
                self.dash_board[index_initial]='O'
                self.player_two_sign.sort()
                if len(self.player_two_sign)==3:
                    if self.check_player_win(self.player_two_sign ):
                        self.whose_win=self.type_of_player2
                        return





        except Exception as e:
            print(type(e).__name__)
    
    def random_position_to(self):
        index_initial_list=[]
        index_list_count=0
        for i in self.dash_board:
            if i=='0':
                index_initial_list.append(index_list_count)
            index_list_count=index_list_count+1
        index_initial=random.choice(index_initial_list)
        return index_initial
                
    
class  XO_game_human_with_computer_intelligent(XO_game_human_with_human):
    def __init__(self,game_mode):
        XO_game_human_with_human.__init__(self,game_mode)
    def set_sign_player2(self):
       
        ##check if can I win
        
        index_to_play=len(self.player_two_sign)
        is_go_to_win=False
        if index_to_play==2:
            for item in self.wins_position:
                if (item[0:3:2]==self.player_two_sign or item[0:3:2]==self.player_two_sign[-1:-3:-1] )  and self.dash_board[item[1]]=='0':
                    self.player_two_sign.append(item[1])
                    self.dash_board[item[1]]='O'
                    is_go_to_win=True
                    self.whose_win=self.type_of_player2
                    print('y win')
                    return
                if (item[0:2:1]==self.player_two_sign or item[0:2:1]==self.player_two_sign[-1:-3:-1] )  and self.dash_board[item[2]]=='0':
                    self.player_two_sign.append(item[2])
                    self.dash_board[item[2]]='O'
                    is_go_to_win=True
                    self.whose_win=self.type_of_player2
                    print('y win')
                    return
                if (item[1:3:1]==self.player_two_sign or item[1:3:1]==self.player_two_sign[-1:-3:-1] )  and self.dash_board[item[0]]=='0':
                    self.player_two_sign.append(item[0])
                    self.dash_board[item[0]]='O'
                    is_go_to_win=True
                    self.whose_win=self.type_of_player2
                    print('y win')
                    return
                    
        if index_to_play==3:
            for item in self.wins_position:
                if self.player_two_sign==item or self.player_two_sign==item[-1:-4:-1] :
                    is_go_to_win=True
                    self.whose_win=self.type_of_player2
                    print('y win')
                    return;
                    
            for item in self.wins_position:
                ##[0:3:2]
                if (item[0:3:2]==self.player_two_sign[0:3:2] or item[0:3:2]==self.player_two_sign[-1:-4:-2] )  and self.dash_board[item[1]]=='0':
                    index_which_will_move=self.player_two_sign[1]
                    self.dash_board[index_which_will_move]='0'
                    self.player_two_sign[1]=item[1]
                    self.dash_board[item[1]]='O'
                    is_go_to_win=True
                    self.whose_win=self.type_of_player2
                    print('y win')
                    return
                if (item[0:2:1]==self.player_two_sign[0:3:2] or item[0:2:1]==self.player_two_sign[-1:-4:-2] )  and self.dash_board[item[2]]=='0':
                    index_which_will_move=self.player_two_sign[1]
                    self.dash_board[index_which_will_move]='0'
                    self.player_two_sign[1]=item[2]
                    self.dash_board[item[2]]='O'
                    is_go_to_win=True
                    self.whose_win=self.type_of_player2
                    return
                if (item[1:3:1]==self.player_two_sign[0:3:2] or item[0:2:1]==self.player_two_sign[-1:-4:-2] )  and self.dash_board[item[0]]=='0':
                    index_which_will_move=self.player_two_sign[1]
                    self.dash_board[index_which_will_move]='0'
                    self.player_two_sign[1]=item[0]
                    self.dash_board[item[0]]='O'
                    is_go_to_win=True
                    self.whose_win=self.type_of_player2
                    print('y win')
                    return
                ##[0:2:1]    
                if (item[1:3:1]==self.player_two_sign[0:2:1] or item[1:3:1]==self.player_two_sign[-2:-4:-1] )  and self.dash_board[item[0]]=='0':
                    index_which_will_move=self.player_two_sign[2]
                    self.dash_board[index_which_will_move]='0'
                    self.player_one_sign[2]=item[0]
                    self.dash_board[item[0]]='O'
                    is_go_to_win=True
                    self.whose_win=self.type_of_player2
                    print('y win')
                    return
                if (item[0:2:1]==self.player_two_sign[0:2:1] or item[0:2:1]==self.player_two_sign[-2:-4:-1] )  and self.dash_board[item[2]]=='0':
                    index_which_will_move=self.player_two_sign[2]
                    self.dash_board[index_which_will_move]='0'
                    self.player_one_sign[2]=item[2]
                    self.dash_board[item[2]]='O'
                    is_go_to_win=True
                    self.whose_win=self.type_of_player2
                    print('y win')
                    return
                if (item[0:3:2]==self.player_two_sign[0:2:1] or item[0:3:2]==self.player_two_sign[-2:-4:-1] )  and self.dash_board[item[1]]=='0':
                    index_which_will_move=self.player_two_sign[2]
                    self.dash_board[index_which_will_move]='0'
                    self.player_one_sign[2]=item[1]
                    self.dash_board[item[1]]='O'
                    is_go_to_win=True
                    self.whose_win=self.type_of_player2
                    print('y win')
                    return
                ##[1:3:1]
                if (item[1:3:1]==self.player_two_sign[1:3:1] or item[1:3:1]==self.player_two_sign[-1:-3:-1] )  and self.dash_board[item[0]]=='0':
                    index_which_will_move=self.player_two_sign[0]
                    self.dash_board[index_which_will_move]='0'
                    self.player_two_sign[0]=item[0]
                    self.dash_board[item[0]]='O'
                    is_go_to_win=True
                    self.whose_win=self.type_of_player2
                    print('y win')
                    return
                if (item[0:2:1]==self.player_two_sign[1:3:1] or item[0:2:1]==self.player_two_sign[-1:-3:-1] )  and self.dash_board[item[2]]=='0':
                    index_which_will_move=self.player_two_sign[0]
                    self.dash_board[index_which_will_move]='0'
                    self.player_two_sign[0]=item[2]
                    self.dash_board[item[2]]='O'
                    is_go_to_win=True
                    self.whose_win=self.type_of_player2
                    print('y win')
                    return
                if (item[0:3:2]==self.player_two_sign[1:3:1] or item[0:3:2]==self.player_two_sign[-1:-3:-1] )  and self.dash_board[item[1]]=='0':
                    index_which_will_move=self.player_two_sign[0]
                    self.dash_board[index_which_will_move]='0'
                    self.player_two_sign[0]=item[1]
                    self.dash_board[item[1]]='O'
                    is_go_to_win=True
                    self.whose_win=self.type_of_player2
                    print('y win')
                    return
                    
## defend on my self : check other player can win
        
        index=self.can_other_player_win(self.player_one_sign,self.dash_board)
        ##print(index)
        if index!=-1:
            self.dash_board[index]='O'
            if len(self.player_two_sign)<3:
                self.player_two_sign.append(index)
                return
            
            else:
                index_move=self.is_player_safe_to_move(self.player_two_sign,self.player_one_sign)
                self.player_two_sign[self.player_two_sign.index(index_move)]=index
                self.dash_board[index_move]='0'
                return                          
        
##May be win next time

        if is_go_to_win==False:
            index=0
            if len(self.player_one_sign)<=2:
                index_initial_list=[]
                index_list_count=0
                for i in self.dash_board:
                    if i=='0':
                        index_initial_list.append(index_list_count)
                    index_list_count=index_list_count+1
                index_initial=random.choice(index_initial_list)
                self.player_two_sign.append(index_initial)
                self.dash_board[index_initial]='O'
                return
            
            len2_index=0
            '''if (len(self.player_two_sign)==2 or len(self.player_one_sign)==2) and self.dash_board[4]=='0':
                print('aliiiiiiiiiiii')
                self.player_two_sign.append(4)
                self.dash_board[4]='O'
                return'''
                
            for item in self.dash_board:
                if item=='0':
                    if len(self.player_two_sign)==3:
                        move=self.is_player_safe_to_move(self.player_two_sign,self.player_one_sign)
                        self.dash_board[move]='0'
                        self.player_two_sign[self.player_two_sign.index(move)]=len2_index
                        self.dash_board[len2_index]='O'
                        return
                    self.dash_board[len2_index]='O'
                    self.player_two_sign.append(len2_index)
                    break;
                len2_index=len2_index+1
                
        
##support method#####################################################################################    
        
            
    def is_player_safe_to_move(self,list_to_check,other_player):
       
        default=list_to_check[0]
        for item in list_to_check:
            new_dash_board=[i for i in self.dash_board]
            new_dash_board[item]='0'
            if self.can_other_player_win(other_player,new_dash_board)==-1:
                return item
            
        return default
    
              
     
            
                       
        
    def can_other_player_win(self,data,new_dash_board):
        index_to_play=len(data)
        is_go_to_win=False
        if index_to_play==2:
            for item in self.wins_position:
                if (item[0:3:2]==data or item[0:3:2]==data[-1:-3:-1] )  and new_dash_board[item[1]]=='0':
                    return item[1]
                if (item[0:2:1]==data or item[0:2:1]==data[-1:-3:-1] )  and new_dash_board[item[2]]=='0':
                    return item[2]                  
                if (item[1:3:1]==data or item[1:3:1]==data[-1:-3:-1] )  and new_dash_board[item[0]]=='0':
                    return item[0]
                    
        if index_to_play==3:        
            for item in self.wins_position:
                ##[0:3:2]
                if (item[0:3:2]==data[0:3:2] or item[0:3:2]==data[-1:-4:-2] )  and new_dash_board[item[1]]=='0':
                    return item[1]
                if (item[0:2:1]==data[0:3:2] or item[0:2:1]==data[-1:-4:-2] )  and new_dash_board[item[2]]=='0':
                    return item[2]
                if (item[1:3:1]==data[0:3:2] or item[0:2:1]==data[-1:-4:-2] )  and new_dash_board[item[0]]=='0':
                    return item[0]
                ##[0:2:1]    
                if (item[1:3:1]==data[0:2:1] or item[1:3:1]==data[-2:-4:-1] )  and new_dash_board[item[0]]=='0':
                    return item[0]
                if (item[0:2:1]==data[0:2:1] or item[0:2:1]==data[-2:-4:-1] )  and new_dash_board[item[2]]=='0':
                    return item[2]
                if (item[0:3:2]==data[0:2:1] or item[0:3:2]==data[-2:-4:-1] )  and new_dash_board[item[1]]=='0':
                    return item[1]
                ##[1:3:1]
                if (item[1:3:1]==data[1:3:1] or item[1:3:1]==data[-1:-3:-1] )  and new_dash_board[item[0]]=='0':
                    return item[0]
                if (item[0:2:1]==data[1:3:1] or item[0:2:1]==data[-1:-3:-1] )  and new_dash_board[item[2]]=='0':
                    return item[2]
                if (item[0:3:2]==data[1:3:1] or item[0:3:2]==data[-1:-3:-1] )  and new_dash_board[item[1]]=='0':
                    return item[1]
        return -1
    

    
            
