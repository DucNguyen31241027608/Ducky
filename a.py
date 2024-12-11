import pygame
import random
from pygame import mixer

#Khởi tạo game
pygame.init()

#Tạo màn hình game
screen = pygame.display.set_mode((800, 600))
background = pygame.image.load('background.png')

#Tiêu đề và biểu tượng game
pygame.display.set_caption("Xử lý rác không gian")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Sound
mixer.music.load("background.wav")
mixer.music.play(-1)

#Nhập từ bàn phím
duoc_nhap = True

#Phi thuyền
spaceship = pygame.image.load('spaceship.png') #Khai báo hình ảnh
spaceshipX = 370 #Tọa độ X của phi thuyền
spaceshipY = 480 #Tọa độ y của phi thuyền
spaceshipX_change = 0
spaceshipY_change = 0

#Xương cá
fishbone = pygame.image.load('fishbone.png')
fishboneX = random.randint(0, 735)
fishboneY = random.randint(50, 150)
fishboneY_change = 1

#Táo
apple = pygame.image.load('apple.png')
appleX = random.randint(0, 735)
appleY = random.randint(50, 150)

#Rác
rac = pygame.image.load('rac.png')
racX = random.randint(0, 735)
racY = random.randint(50, 150)

#Đạn
bullet = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = 'ready'

#Điểm số
diem = 0
font = pygame.font.Font('Freesansbold.ttf',32)
testX = 10
testY = 10
def show_diem(x,y):
    score = font.render('Score:' + str(diem), True, (255, 255, 255))
    screen.blit(score, (x, y))

#Game over text
over_font = pygame.font.Font('Freesansbold.ttf',64)
over = over_font.render('GAME OVER', True, (255, 255, 255))

#Chơi lại
replay = pygame.font.Font('Freesansbold.ttf',32)
lai = replay.render('If you want to play again press space bar', True, (255, 255, 255))
    
#Chương trình vẽ các đối tượng
def Phi_thuyen(x,y):
    screen.blit(spaceship, (x, y)) #Vẽ phi thuyền lên màn hình

def Xuong_ca(x,y):
    screen.blit(fishbone, (x, y))

def tao(x,y):
    screen.blit(apple, (x, y))

def racthai(x,y):
    screen.blit(rac, (x, y))

def ban(x,y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bullet,(x + 16 , y + 10))
    
def ban_trung(fishboneX,fishboneY,bulletX,bulletY):
    khoang_cach = ((fishboneX-bulletX)**2+(fishboneY-bulletY)**2)**0.5
    if khoang_cach < 27:
        return True
    else:
        return False
    
def ban_tao(appleX,appleY,bulletX,bulletY):
    khoang_cach = ((appleX-bulletX)**2+(appleY-bulletY)**2)**0.5
    if khoang_cach < 27:
        return True
    else:
        return False
    
def ban_rac(racX,racY,bulletX,bulletY):
    khoang_cach = ((racX-bulletX)**2+(racY-bulletY)**2)**0.5
    if khoang_cach < 27:
        return True
    else:
        return False

def dung_nhau(fishboneX,fishboneY,spaceshipX,spaceshipY):
    distance = (((fishboneX+16)-(spaceshipX+32))**2+((fishboneY+32)-spaceshipY)**2)**0.5
    if distance < 20:
        return True
    else:
        return False
    
def dung_tao(appleX,appleY,spaceshipX,spaceshipY):
    distance = (((appleX+16)-(spaceshipX+32))**2+((appleY+32)-spaceshipY)**2)**0.5
    if distance < 20:
        return True
    else:
        return False   
    
def dung_rac(racX,racY,spaceshipX,spaceshipY):
    distance = (((racX+16)-(spaceshipX+32))**2+((racY+32)-spaceshipY)**2)**0.5
    if distance < 20:
        return True
    else:
        return False   

#Game loop
running = True
while running: #Vòng lặp chương trình game để không bị tắt giữa chừng
    
    #Hiện background
    screen.blit(background,(0,0))
    
    for event in pygame.event.get(): #Trong tất cả các hành động (nhấn phím,di chuột, đóng game,...)
        if event.type == pygame.QUIT: #Nếu bấm quit chương trình sẽ tắt
            running = False
        if duoc_nhap:
            #Điều khiển  phi thuyền
            if event.type == pygame.KEYDOWN: #Lệnh chạy khi nhập gì đó từ bàn phím (KEYDOWN: Là một event dùng để bắt đầu hành động, ví dụ như di chuyển hoặc thay đổi trạng thái)
                if event.key == pygame.K_LEFT:
                    spaceshipX_change = -5
                if event.key == pygame.K_RIGHT:
                    spaceshipX_change = 5
                if event.key == pygame.K_UP:
                    spaceshipY_change = -5
                if event.key == pygame.K_DOWN:
                    spaceshipY_change = 5
            # Điều khiển đạn
                if event.key == pygame.K_SPACE:
                    if bullet_state == 'ready':
                        bulletSound = mixer.Sound("laser.wav")
                        bulletSound.play()
                        bulletX = spaceshipX # Tọa độ đường đạn tại thời điểm bắn không thay dổi theo trục x của phi thuyền
                        bulletY = spaceshipY
                        ban(bulletX, bulletY)
        else:
             if event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_SPACE:
                     diem = 0
                     fishboneY_change = 1
                     duoc_nhap = True
                     fishboneX = random.randint(0, 735)
                     fishboneY = random.randint(50, 150)
                     appleX = random.randint(0, 735)
                     appleY = random.randint(50, 150)
                     racX = random.randint(0, 735)
                     racY = random.randint(50, 150)
                    
        if event.type == pygame.KEYUP: #Lệnh chạy khi không nhấn phím gì (KEYUP: Là một event dùng để kết thúc hành động, ví dụ như dừng di chuyển hoặc ngừng thay đổi trạng thái.)
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                spaceshipX_change = 0
                spaceshipY_change = 0 
    
    #Cập nhật vị trí phi thuyền           
    spaceshipX += spaceshipX_change
    spaceshipY += spaceshipY_change
    if spaceshipX <= 0: #Giữ cho phi thuyền di chuyển trong một khoảng không bị out ra khung hình
        spaceshipX = 0
    elif spaceshipX >= 736:
        spaceshipX = 736
    if spaceshipY <= 50:
        spaceshipY = 50
    elif spaceshipY >= 536:
        spaceshipY = 536
    
    # Game Over
    thua = dung_nhau(fishboneX,fishboneY,spaceshipX,spaceshipY)
    thua_1 = dung_tao(appleX,appleY,spaceshipX,spaceshipY)
    thua_2 = dung_rac(racX,racY,spaceshipX,spaceshipY)
    if thua or thua_1 or thua_2:
        screen.blit(over, (200, 250))
        screen.blit(lai, (90, 350))
        fishboneY_change = 0
        duoc_nhap = False
    
    #Cập nhật vị trí xương các vật thể    
    else:
        fishboneY += fishboneY_change
        appleY += fishboneY_change
        racY += fishboneY_change
        if fishboneY >=600:
            fishboneX = random.randint(0, 735)
            fishboneY = random.randint(50, 150)
        if appleY >= 600:
            appleX = random.randint(0, 735)
            appleY = random.randint(50, 150)
        if racY >= 600:
            racX = random.randint(0, 735)
            racY = random.randint(50, 150)
    
    # Tăng độ khó        
    if diem >= 10:
        fishboneY_change = 1.5
    if diem >= 15:
        fishboneY_change = 2
    if diem >= 20:
        fishboneY_change = 2.5
    if diem >= 25:
        fishboneY_change = 3
    if diem >= 30:
        fishboneY_change = 3.5
    
    #Cập nhật vị trí đạn bay
    if bulletY <=0:
        bulletY = 480
        bullet_state = 'ready'
    if bullet_state == 'fire':
       ban(bulletX,bulletY)
       bulletY -= bulletY_change
       
    #Bắn trúng
    va_cham = ban_trung(fishboneX,fishboneY,bulletX,bulletY)
    va_tao = ban_tao(appleX,appleY,bulletX,bulletY)
    va_rac = ban_rac(racX,racY,bulletX,bulletY)
    if va_cham:
        explosionSound = mixer.Sound("explosion.wav")
        explosionSound.play()
        bulletY = 480
        bullet_state = 'ready'
        diem += 1
        #Sau khi bắn trúng sẽ xuất hiện mục tiêu mới
        fishboneX = random.randint(0, 735)
        fishboneY = random.randint(50, 150)
    if va_tao:
        explosionSound = mixer.Sound("explosion.wav")
        explosionSound.play()
        bulletY = 480
        bullet_state = 'ready'
        diem += 1
        appleX = random.randint(0, 735)
        appleY = random.randint(50, 150)
    if va_rac:
        explosionSound = mixer.Sound("explosion.wav")
        explosionSound.play()
        bulletY = 480
        bullet_state = 'ready'
        diem += 1
        racX = random.randint(0, 735)
        racY = random.randint(50, 150)
    
    Phi_thuyen(spaceshipX, spaceshipY)
    Xuong_ca(fishboneX,fishboneY,)
    tao(appleX,appleY)
    racthai(racX,racY)
    show_diem(testX, testY)
    
    pygame.display.update()
    
    