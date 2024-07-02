import math
import random
import pygame, sys
from pygame.locals import QUIT

pygame.init()
def mousecollide(hitbox):
    temp_output=False
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
           pygame.quit()
           sys.exit()
        elif event.type==pygame.MOUSEBUTTONDOWN:
            if hitbox.collidepoint(pygame.mouse.get_pos()):
                temp_output=True
    return temp_output

def mousehold(hitbox):
    if pygame.mouse.get_pressed()[0]:
        if hitbox.collidepoint(pygame.mouse.get_pos()):
            return True
        else:
            return False
    else:
        return False

def mousehover(object):
    if object.collidepoint(pygame.mouse.get_pos()):
        return True
    else:
        return False


recipe_input_valid=["lead0000carbon00"]
recipe_output_valid=["steel000"]
recipe_input=""
def recipe(string):
    try:
        return recipe_output_valid[recipe_input_valid.index(string)]
    except:
        return False

def flip_even_string(string):
    return string[(len(string)//2):len(string)]+string[0:len(string)//2]


screen_x=1152
screen_y=576

cloud_1_y=random.randint(0,screen_y//1.5)
cloud_2_y=random.randint(0,screen_y//1.5)

game_state_change_1_2=False
base_play_button_hitbox_y=412
base_subtitle_hitbox_y=284
base_title_hitbox_y=16
base_cloud_1_hitbox_x=screen_x
base_cloud_2_hitbox_x=screen_x*random.choice([1.25,1.5,1.75])
cloud_1_x_speed=3
cloud_2_x_speed=3
screen = pygame.display.set_mode((screen_x,screen_y))
pygame.display.set_caption('     Lead to Gold: An alchemist\'s folly')
tick=0
title_screen_y_veloc=0
start_title_animation=False
game=0
sky_red=135
sky_green=206
sky_blue=245
carbon_hold=False
lead_hold=False

cloud_1_picture=open("lead to gold cloud 1.png")
cloud_1=pygame.image.load(cloud_1_picture)

cloud_2_picture=open("lead to gold cloud 2.png")
cloud_2=pygame.image.load(cloud_2_picture)

title_picture=open("lead to gold title.png")
title=pygame.image.load(title_picture)

subtitle_picture=open("lead to gold subtitle.png")
subtitle=pygame.image.load(subtitle_picture)

play_button_picture=open("play button.png")
play_button=pygame.image.load(play_button_picture)

opening_background=pygame.Rect(0,0,screen_x,screen_y)
game_background=pygame.Rect(0,0,screen_x,screen_y)

while True:

    tick+=1
    clock=pygame.time.Clock()

    if game==0:
        pygame.draw.rect(screen,(sky_red,sky_green,sky_blue),opening_background)

        cloud_1_hitbox=pygame.Rect(base_cloud_1_hitbox_x,cloud_1_y,256,128)
        cloud_2_hitbox=pygame.Rect(base_cloud_2_hitbox_x,cloud_2_y,256,128)
        if abs(cloud_1_hitbox.y-cloud_2_hitbox.y)<200:
            cloud_1_hitbox.y-=200

        cloud_1_y+=0.5*math.sin(tick/10)
        base_cloud_1_hitbox_x-=cloud_1_x_speed

        if cloud_1_hitbox.x<-320 and start_title_animation==False:
            base_cloud_1_hitbox_x=screen_x
            cloud_1_y=random.randint(0,screen_y//1.5)
            cloud_1_x_speed=3*(random.choice([0.5,1,1.5]))

            if abs(cloud_1_hitbox.y-cloud_2_hitbox.y)<200:
                cloud_1_hitbox.y-=200

        cloud_2_y+=0.5*math.sin((tick/10)+1)
        base_cloud_2_hitbox_x-=cloud_2_x_speed

        if cloud_2_hitbox.x<-320 and start_title_animation==False:
            base_cloud_2_hitbox_x=screen_x
            cloud_2_y=random.randint(0,screen_y//1.5)
            cloud_2_x_speed=2*(random.choice([0.5,1,1.5]))


        screen.blit(cloud_1,(base_cloud_1_hitbox_x,cloud_1_y))
        screen.blit(cloud_2,(cloud_2_hitbox.x,cloud_2_hitbox.y))

        title_hitbox=pygame.Rect((screen_x-1152)/2,base_title_hitbox_y+(16*math.sin(tick/30)),1152,256)
        screen.blit(title,(title_hitbox.x,title_hitbox.y))

        subtitle_hitbox=pygame.Rect((screen_x-1024)/2,base_subtitle_hitbox_y+(12*math.sin(tick/30)),1024,128)
        screen.blit(subtitle,(subtitle_hitbox.x,subtitle_hitbox.y))

        play_button_hitbox=pygame.Rect((screen_x-256)/2,base_play_button_hitbox_y+(9*math.sin(1+tick/30)),256,128)
        screen.blit(play_button,(play_button_hitbox.x,play_button_hitbox.y))

        if mousecollide(play_button_hitbox):
            start_title_animation=True
            title_screen_y_veloc=max(title_screen_y_veloc,2)
        if start_title_animation==True:
            title_screen_y_veloc+=1/4
            
            sky_blue=max(sky_blue-0.1,205)
            sky_red=min(sky_red+0.2,150)

        if title_screen_y_veloc!=0:
            base_title_hitbox_y-=title_screen_y_veloc
            base_subtitle_hitbox_y-=title_screen_y_veloc*1.05
            base_play_button_hitbox_y-=title_screen_y_veloc*1.1
            cloud_1_y-=title_screen_y_veloc*0.3
            cloud_2_y-=title_screen_y_veloc*0.25
        if start_title_animation==True and max(cloud_2_y,cloud_1_y)<-320 and play_button_hitbox.y<-256:
            game=1
            title_picture.close()
            subtitle_picture.close()
            play_button_picture.close()
            cloud_1_picture.close()
            cloud_2_picture.close()
            del title,subtitle,play_button,cloud_1,cloud_2,     

            table_hitbox=pygame.Rect((screen_x-1152)/2,576,1152,128)
            table_picture=open("lead to gold table.png")
            table=pygame.image.load(table_picture)
            table_move_tick=-1920
            move_table=True

            machine_1_hitbox=pygame.Rect(384,-768,384,384)
            machine_1_picture=open("lead to gold machine 1.png")
            machine_1=pygame.image.load(machine_1_picture)
            machine_1_velocity=0
            move_machine_1=False

            machine_1_collider=pygame.Rect(machine_1_hitbox.x+328,machine_1_hitbox.y+992,32,48)
            machine_1_direction_collider=pygame.Rect(machine_1_hitbox.x+312,machine_1_hitbox.y+984,8,64)

            substance_gravity=3

            lead_hitbox=pygame.Rect(screen_x//1.25,-128,64,64)
            lead_picture=open("substances\lead to gold lead.png")
            lead=pygame.image.load(lead_picture)   
            lead_colour=(34,34,33)
            lead_velocity=0
            collide_lead_on_machine=True
            draw_lead=True
            play_lead_movement=False

            arrow_hitbox_base_x=800
            arrow_hitbox=pygame.Rect(arrow_hitbox_base_x+screen_x,216,144,64)
            arrow_picture=open("lead to gold arrow.png")
            arrow=pygame.image.load(arrow_picture)
            move_arrow=False
            arrow_hover=False
            flip_arrow=False
            draw_flip_arrow=False

            left_arrow_hitbox_base_x=0
            left_arrow_hitbox=pygame.Rect(left_arrow_hitbox_base_x+0,216,144,64)
            left_arrow=pygame.transform.flip(arrow,True,False)

            carbon_hitbox=pygame.Rect(144,-128,64,64)
            carbon_picture=open("substances\lead to gold carbon.png")
            carbon=pygame.image.load(carbon_picture)
            carbon_velocity=0
            next_substance=False
            play_carbon_movement=False
            collide_carbon_on_machine=True


            machine_1_carbon_collider=pygame.Rect(machine_1_hitbox.x+24,machine_1_hitbox.y+992,32,48)
            machine_1_carbon_direction_collider=pygame.Rect(machine_1_hitbox.x+64,machine_1_hitbox.y+984,8,64)
            
            

    elif game==1:                   # idk what this shit does anymore just pretend it doesn't exist and look at the 𝓕𝓪𝓷𝓬𝔂 class definitions and following OOP further down pls
        if move_table and table_hitbox.y>screen_y-128:
            table_move_tick+=128
            table_hitbox.y=max(screen_y-max(table_move_tick,0)**0.6,screen_y-128)
            if table_hitbox.y==screen_y-128:
                move_table=False
                move_machine_1=True

        if move_machine_1:
            machine_1_velocity+=1
            machine_1_hitbox.y=min(machine_1_hitbox.y+machine_1_velocity,64)
            if machine_1_hitbox.y==64:
                move_machine_1=False
                move_arrow=True

        if move_arrow:
            arrow_hitbox.x=max(800,arrow_hitbox.x-10)
            if arrow_hitbox.x==800:
                move_arrow=False
                arrow_hover=True
                
        if arrow_hover:
            arrow_hitbox.x=arrow_hitbox_base_x+16*math.sin(tick/32)


        if not play_lead_movement and mousehold(lead_hitbox):
            lead_hold=True
        if lead_hold:
            lead_hitbox.y=min(pygame.mouse.get_pos()[1]-32,screen_y-64)
            lead_hitbox.x=min(max(pygame.mouse.get_pos()[0]-32,0),screen_x-64)
            if not pygame.mouse.get_pressed()[0] or play_lead_movement:
                lead_hold=False
        else:
            if pygame.Rect.colliderect(lead_hitbox,table_hitbox):
                lead_hitbox.y=table_hitbox.y-63
                lead_velocity=0
            else:
                if not play_lead_movement:
                    lead_velocity+=substance_gravity
                    lead_hitbox.y+=lead_velocity
                else:
                    lead_velocity=0

        if play_lead_movement:
            lead_hitbox.y=216
            lead_hitbox.x-=1
            if lead_hitbox.x<548:
                play_lead_movement=False
                collide_lead_on_machine=True
                flip_arrow=True
                lead_hitbox.x=9999
                lead_hitbox.y=9999

        if flip_arrow:
            arrow_hover=False
            arrow_hitbox.x-=5
            if arrow_hitbox.x<machine_1_hitbox.x+96:
                draw_flip_arrow=True
            if arrow_hitbox.x<192:
                arrow_hitbox_base_x=192
                flip_arrow=False
                arrow_hover=True
                next_substance=True


        if next_substance and not play_carbon_movement and mousehold(carbon_hitbox):
            carbon_hold=True
        if carbon_hold:
            carbon_hitbox.y=min(pygame.mouse.get_pos()[1]-32,screen_y-64)
            carbon_hitbox.x=min(max(pygame.mouse.get_pos()[0]-32,0),screen_x-64)      
            carbon_velocity=0
            if not pygame.mouse.get_pressed()[0] or play_carbon_movement:
                carbon_hold=False
        elif next_substance and not play_carbon_movement:
            carbon_velocity+=substance_gravity
            carbon_hitbox.y+=carbon_velocity
            if pygame.Rect.colliderect(carbon_hitbox,table_hitbox):
                carbon_velocity=0
                carbon_hitbox.y=table_hitbox.y-63
        if play_carbon_movement:
            carbon_hitbox.x+=1
            carbon_hitbox.y=216
            carbon_velocity=0
            if carbon_hitbox.x==548:
                play_carbon_movement=False   
                collide_carbon_on_machine=True
                game_state_change_1_2=True
                carbon_hitbox.x=9998
                carbon_hitbox.y=9998
                          

        if collide_carbon_on_machine and pygame.Rect.colliderect(carbon_hitbox,machine_1_carbon_collider) and not pygame.Rect.colliderect(carbon_hitbox,machine_1_carbon_direction_collider):
            recipe_input+="carbon00"
            if len(recipe_input)==16:
                recipe(recipe_input)
                recipe_input=""
            collide_carbon_on_machine=False
            play_carbon_movement=True
            #print(recipe_input)




        if collide_lead_on_machine and pygame.Rect.colliderect(lead_hitbox,machine_1_collider) and not pygame.Rect.colliderect(lead_hitbox,machine_1_direction_collider):
            recipe_input+="lead0000"
            if len(recipe_input)==16:
                print(recipe(recipe_input))
                recipe_input=""
            collide_lead_on_machine=False
            play_lead_movement=True
            #print(recipe_input)

        pygame.draw.rect(screen,(sky_red,sky_green,sky_blue),opening_background)

        if draw_lead:
            screen.blit(lead,(lead_hitbox.x,lead_hitbox.y))
        screen.blit(carbon,(carbon_hitbox.x,carbon_hitbox.y))

        screen.blit(table,(table_hitbox.x,table_hitbox.y))
        
        if not draw_flip_arrow:
            screen.blit(arrow,(arrow_hitbox.x,arrow_hitbox.y))
        else:    
            screen.blit(left_arrow,(arrow_hitbox.x,arrow_hitbox.y))

        screen.blit(machine_1,(machine_1_hitbox.x,machine_1_hitbox.y))

        # pygame.draw.rect(screen,(64,64,0),machine_1_collider)
        # pygame.draw.rect(screen,(255,0,0),machine_1_direction_collider)

        # pygame.draw.rect(screen,(64,64,0),machine_1_carbon_collider)
        # pygame.draw.rect(screen,(255,0,0),machine_1_carbon_direction_collider)



        if game_state_change_1_2:



            game=2


            left_machine_hitbox=pygame.Rect(machine_1_hitbox.x+24,machine_1_hitbox.y+992-832,32,48)
            left_machine_direction_hitbox=pygame.Rect(machine_1_hitbox.x+64,machine_1_hitbox.y+984-832,8,64)

            right_machine_hitbox=pygame.Rect(machine_1_hitbox.x+328,machine_1_hitbox.y+992-832,32,48)
            right_machine_direction_hitbox=pygame.Rect(machine_1_hitbox.x+312,machine_1_hitbox.y+984-832,8,64)
            
            recipe_string=""

            recipe_result=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
            recipe_ingredients=["not_craftable","not_craftable","lead0000carbon00","steel000carbon00","fire0000fire0000","energy00fire0000","life0000carbon00","fire0000carbon00",
                                "oxygen00death000","water000energy00","water000magic000","life0000fire0000","sulfur00carbon00","hydrogenhydrogen","energy00life0000","magic000steel000",
                                "oxygen00fire0000","osmium00osmium00","steel000water000","life0000nitrogen","dirt0000water000","silicon0mud00000","silicon0steel000","compsci0stone000",
                                "philosoplead0000"]

            substance_count=64

            gold_created=False

            substance_gravity=3

            substance_id_hold_table=[]

            for e in range(0,substance_count):
                substance_id_hold_table.append(False)

            substance_id_move_table=[]

            for e in range(0,substance_count):
                substance_id_move_table.append([False,False])

            substance_id_y_velocity_table=[]

            for e in range(0,substance_count):
                substance_id_y_velocity_table.append(0)

            all_substance_table=[]  #only for function definitions - definiton occurs later

            substance_table=[]


            def add_substance(id,x,y):
                global substance_table
                temp=[all_substance_table[id],pygame.image.load(open(all_substance_table[id].image))]  # Note: THIS IS ONLY HERE FOR CLASS DEFINITION - THE REAL ONE IS FOUND BELOW
                temp[0].x=x
                temp[0].y=y
                temp[0].rect.x=x
                temp[0].rect.y=y
                substance_table.append([all_substance_table[id],pygame.image.load(open(all_substance_table[id].image))]) #impliments file loading       

            class substance:
                def __init__(self,x,y,image,string,id):
                    self.x=x
                    self.y=y
                    self.image=image
                    self.rect=pygame.Rect(self.x,self.y,64,64)
                    self.string=string
                    self.id=id


                def add_recipe(self):
                    global recipe_string
                    recipe_string+=self.string
                    if len(recipe_string)==16:
                        try:
                            add_substance(recipe_result[recipe_ingredients.index(recipe_string)],548,216)
                            recipe_string=""
                        except:
                            try:
                                add_substance(recipe_result[recipe_ingredients.index(flip_even_string(recipe_string))],548,216)
                                recipe_string=""
                            except:
                                recipe_string=""

                        recipe_string=""


                def hold(self):
                    global substance_id_hold_table

                    if mousehold(self.rect) and sum(substance_id_hold_table)==0:
                        substance_id_hold_table[self.id]=True

                    if substance_id_hold_table[self.id]:
                        if not pygame.mouse.get_pressed()[0] or substance_id_move_table[self.id][0]==True or substance_id_move_table[self.id][1]==True:
                            substance_id_hold_table[self.id]=False
                        else:
                            self.rect.x=min(max(pygame.mouse.get_pos()[0]-32,0),screen_x-64)
                            self.rect.y=min(pygame.mouse.get_pos()[1]-32,screen_y-64)
                    #return substance(self.x,self.y,self.image,self.string,self.id)                        


                def left_movement(self):
                    if pygame.Rect.colliderect(self.rect,left_machine_hitbox)and not pygame.Rect.colliderect(self.rect,left_machine_direction_hitbox):
                        substance_id_move_table[self.id][0]=True
                    if substance_id_move_table[self.id][0]:
                        self.rect.x+=1
                        self.rect.y=216
                        if self.rect.x==548:
                            self.rect.x=((144+(912+random.randint(-64,0))*random.randint(0,1)))
                            self.rect.y=-128
                            substance_id_move_table[self.id][0]=False
                            self.add_recipe()

                    #return substance(self.x,self.y,self.image,self.string,self.id)                       

                def right_movement(self):
                    if pygame.Rect.colliderect(self.rect,right_machine_hitbox)and not pygame.Rect.colliderect(self.rect,right_machine_direction_hitbox):
                        substance_id_move_table[self.id][1]=True
                    if substance_id_move_table[self.id][1]:
                        self.rect.x-=1
                        self.rect.y=216                        
                        if self.rect.x==548:
                            self.rect.x=((144+(912+random.randint(-64,0))*random.randint(0,1)))
                            self.rect.y=-128                            
                            substance_id_move_table[self.id][1]=False
                            self.add_recipe()

                    #return substance(self.x,self.y,self.image,self.string,self.id)

                def gravity(self):
                    if substance_id_hold_table[self.id]:
                        substance_id_y_velocity_table[self.id]=0

                    elif substance_id_move_table[self.id][0] or substance_id_move_table[self.id][1] or pygame.Rect.colliderect(self.rect,table_hitbox):
                        substance_id_y_velocity_table[self.id]=0
                        self.rect.y=min(table_hitbox.y-63,self.rect.y)
                    else:
                        substance_id_y_velocity_table[self.id]+=substance_gravity
                        self.rect.y+=substance_id_y_velocity_table[self.id]
                    #return substance(self.x,self.y,self.image,self.string,self.id)

            def add_substance(id,x,y):
                global substance_table
                global gold_created
                duplicate_substance=False
                for e in range(0,len(substance_table)):
                    if substance_table[e][0].id==id:
                        duplicate_substance=True                
                        break
                if not duplicate_substance:
                    temp=[all_substance_table[id],pygame.image.load(open(all_substance_table[id].image))]
                    temp[0].x=x
                    temp[0].y=y
                    temp[0].rect.x=x
                    temp[0].rect.y=y

                    substance_table.append(temp) #impliments file loading 

                if id ==24:
                    gold_created=True  
          


            all_substance_table=[substance(640,-64,"substances\lead to gold lead.png","lead0000",0),substance(144,-64,"substances\lead to gold carbon.png","carbon00",1),
                                 substance(548,216,"substances\lead to gold steel.png","steel000",2),substance(0,0,"substances\lead to gold fire.png","fire0000",3),
                                 substance(0,0,"substances\lead to gold energy.png","energy00",4),substance(0,0,"substances\lead to gold life.png","life0000",5),
                                 substance(0,0,"substances\lead to gold silicon.png","silicon0",6),substance(0,0,"substances\lead to gold water.png","water000",7),
                                 substance(0,0,"substances\lead to gold nitrogen.png","nitrogen",8),substance(0,0,"substances\lead to gold oxygen.png","oxygen00",9),
                                 substance(0,0,"substances\lead to gold hydrogen.png","hydrogen",10),substance(0,0,"substances\lead to gold death.png","death000",11),
                                 substance(0,0,"substances\lead to gold explosive.png","explosiv",12),substance(0,0,"substances\lead to gold helium.png","helium00",13),
                                 substance(0,0,"substances\lead to gold magic.png","magic000",14),substance(0,0,"substances\lead to gold osmium.png","osmium00",15),
                                 substance(0,0,"substances\lead to gold sulfur.png","sulfur00",16),substance(0,0,"substances\lead to gold uranium.png","uranium0",17),
                                 substance(0,0,"substances\lead to gold mercury.png","mercury0",18),substance(0,0,"substances\lead to gold dirt.png","dirt0000",19),
                                 substance(0,0,"substances\lead to gold mud.png","mud00000",20),substance(0,0,"substances\lead to gold stone.png","stone000",21),
                                 substance(0,0,"substances\lead to gold compsci.png","compsci0",22),substance(0,0,"substances\lead to gold philosopher.png","philosop",23),
                                 substance(0,0,"substances\lead to gold gold.png","gold0000",24)]    


            add_substance(0,144,-128)
            add_substance(1,800,-128)           
            add_substance(2,548,216)

            
            
            def draw_substance(index):
                screen.blit(substance_table[index][1],(substance_table[index][0].rect.x,substance_table[index][0].rect.y))            




            game_state_change_1_2=False

    elif game==2:

        pygame.draw.rect(screen,(sky_red,sky_green,sky_blue),game_background)

        for e in range(0,len(substance_table)):

            substance_table[e][0].gravity()
            substance_table[e][0].hold()
            substance_table[e][0].left_movement()
            if not substance_id_move_table[substance_table[e][0].id][0]:
                substance_table[e][0].right_movement()            

            draw_substance(e)


        screen.blit(table,(table_hitbox.x,table_hitbox.y))

        screen.blit(machine_1,(machine_1_hitbox.x,machine_1_hitbox.y))

        # debug draw things
        
        # pygame.draw.rect(screen,(255,0,0),left_machine_hitbox)
        # pygame.draw.rect(screen,(255,0,0),left_machine_direction_hitbox)

        # pygame.draw.rect(screen,(255,0,0),right_machine_hitbox)
        # pygame.draw.rect(screen,(255,0,0),right_machine_direction_hitbox)

        #pygame.draw.rect(screen,(255,0,0),substance_table[1][0].rect)


        if gold_created:
            game=3
            message_move=True
            message_hitbox=pygame.Rect(0,-768,1152,512)
            message_image=pygame.image.load(open("lead to gold end screen.png"))

    elif game==3:

        pygame.draw.rect(screen,(sky_red,sky_green,sky_blue),game_background)

        for e in range(0,len(substance_table)):
            substance_table[e][0].gravity()
            draw_substance(e)

        screen.blit(table,(table_hitbox.x,table_hitbox.y))

        screen.blit(machine_1,(machine_1_hitbox.x,machine_1_hitbox.y))        

        if message_move:
            message_hitbox.y+=4    
            table_hitbox.y+=6
            machine_1_hitbox.y+=6
            if message_hitbox.y>0:
                message_move=False
        else:
            message_hitbox.y=10*math.sin(tick/15)


        screen.blit(message_image,(message_hitbox.x,message_hitbox.y))


    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
