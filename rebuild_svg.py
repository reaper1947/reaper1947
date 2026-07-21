import os

ascii_art = """                                  .=*###:                                                           
                             :=*#%%%%%@@%%%%%%##*-=.                                                
                         .=*#%%%%%%%%%%@@%%%%%%%%#*=.                                               
                      .=##%%%%%%%%%%%%%%%%%%%%%%%%%%#=.                                             
                    -#%%%#%%%%%%%%%%%%###%%%%%%%%%%%%##+.                                           
                  =#%%#%%%%%%%%%%%%%%%%%%##%%%%%%%%%%#%##*-                                         
               .=#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#%%%###*-                                       
              -#%%%%%#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#%#####+.                                     
            :=#%%%@%%%%%%%%%%%%@@%%%%%%%%%%%%%%%%%%%%%##%#####=:                                    
           -=#%%@@%@%%%@%%%@%%%%%%%%%#%%%###%%%%%%%%%%%##%%%###=.                                   
          :*%%@@@@@@@@@@%@@%@%%%%%%%%#########%%%%%%%%%%#%%%%%%*:                                   
          +%%@@@@@@@@@@@@@%@%%%%%%%%%%#########%%@@@@@%%%%%@%@%#-                                   
         -%%@@@@@@@@@@@@@%@@@@@%@@@@%***#*######%%@@@@@@@@@@@@%%+                                   
        .#@@@@@@@@@@@%@@%@@%%%%%@@@@%*********#%%@@@@@@@@@@@@@@%%.                                  
        =%@@@@@@@@@%@@%%%@%####%@%@@%##***#***###%%%%%%@@@@@@@@@%-                                  
        *%@@@@@@@@@%@%##%%###*#%#%%%%##***+***#######**###%@@@@@@-                                  
        =%@@@@@@@@%@%%######**#########*+===+**#####**+++++#@@@@%.                                  
        .#@@@@@@@@%#****##%%@@@@#%%#*#**==--=+*#%%@@@@%#++++%@@@*                                   
          *@@@@@@%#****#%@%#@@@%+#%#***++=--===#%%@@@++##*==+%%%-                                   
          .#@@@@@#*+++*************+++++=----====+*++===-----#%*.                                   
           *##%@%*+++==========+++++++++=--:-----===----::---*#:                                    
           +###@%++++===--=========+++++=--:--------==--:::--+=                                     
           =##*##++++=============+++*++=--:---=---------:---=:                                     
           +#*+*#***+++====-======+*++=+===-----=------------=.                                     
           =#+*##****++====---===+**+++**++===+=-=---------===.                                     
           -**##*****+++========++***#@@%#**#@@*+=--------===-.                                     
           :++********+++=======+++*####**+==***+---------===-.                                     
            =++++******+++=========++++==----------------===--.                                     
            .++++******+++========+++++==-=----------===-===+:                                      
              :=*%******+++===+++++++++++=====--------======.                                       
                 .******++++++*******####*+****+====-=======                                        
                  -********+**##%%%%######******#**++=====+:                                        
                  .********+*#########***#*++**###%%#+==+=.                                         
                   =********+++*****#*#****++**++++**++++:                                          
                   :*********+++++*******+*++++=====++++:                                           
                   :*#****#***++++++*******+++======+++-                                            
                   -*###**##***+++++++++++++=======+++-                                             
                   -**###*##*****++++============++++=.                                             
                   +***######******++++========++++++=.                                             
                   +******####********+++++++++++++===                                              
                   +********##***********+++++++++==+-                                              
                  .***************************++=====:                                              
                  -**************#####**##*++++=====+:                                              
                 -******************##****++++======+:                                              
               .+************************+++++=======:*%+-.                                         
            .-+**********************+++++++=========+-:%%%%%#+-.                                   
         .----=********+*++*++++++++++++++============#=-%%%%%%%%%+::::.                            
   -#%%=-------=******+++++++++++++++++++=============*#=-%%%%%%%%%%#:::::::.                       
+%@@@@#----------+++*+++++++++++++++++++++============*#*.-#%%%%%%%%%#=:::::::::::..                
%@@@@@%=:::------:=+++++++++++++=++=+=================**+.:-#%%%%%%%%%%*::::::::::::::              
%@@@@@%+-::::-----::++++++++++++==================--==*+:::.:#%%%%%%%%%%%=::::::::::::::            
%@@@@@%*--::::::---:::+++++++================---=---=+=..:...:%%%%%%%%%%%%=::::::::::.::-.          
%@%@@@%#-=-:::::::--::::=++++===============-------==:.::.....-%%%%%%%%%%%%+::::::..:..::-:         
%%@@@%%#==-:::::::::::::::-======-======----------:..:::.....::-%%%%%%%%%%%%+:::::::::.:::-:        
%%%%%%%#=-::::::::::::::::::::-----------------:..:::::.....::..-%%%%%@%%%%%%+-:::::::.::::--       
%%%%%%%#-::::::::..:::::::::::::::..::::::.....:::::.......::....=%%%%%@%%%%%%=:::::::.::::---      
%%%%%%%#-:---:::::...::::::::::::::::::::::::::::.........:::..:.:#%%%%%@%%%%%%=::::::.:::::---.    
%%%%%%%#------:::::::....:::.......:::::::::::..........:::::....::#%%%%%@%%%%%#--::::.:::::----:   
%%%%%%%*------:::::::::...............:::...:.........:::::::....::=%%%%%%%%%%%%%--:::.:::::-----:  
%%%%%%%*:::----::.:::::::::......................:.::..:::::....::-:*%%%%%%%%%%%%*-:::::::-:------: 
%%%%%%%*::::---::...::::.::::::.......::........:::::::::::......:-:=#%%%%%%%%%%%%+-::::::-:-------:"""

lines = [line for line in ascii_art.split('\n') if line]

def make_svg(dark=True):
    bg_color = "#161b22" if dark else "#ffffff"
    text_color = "#c9d1d9" if dark else "#24292e"
    
    # 61 lines * 15px = 915px height, plus padding
    height = 950
    # Longest string in ascii is 100 chars, so ~700px width. Info takes ~600px
    width = 1350
    x_offset_ascii = 15
    y_start_ascii = 30
    
    x_offset_info = 750
    
    svg = f'''<?xml version='1.0' encoding='UTF-8'?>
<svg xmlns="http://www.w3.org/2000/svg" font-family="ConsolasFallback,Consolas,monospace" width="{width}px" height="{height}px" font-size="14px">
<style>
@font-face {{
src: local('Consolas'), local('Consolas Bold');
font-family: 'ConsolasFallback';
font-display: swap;
-webkit-size-adjust: 109%;
size-adjust: 109%;
}}
.key {{fill: #ffa657;}}
.value {{fill: #a5d6ff;}}
.addColor {{fill: #3fb950;}}
.delColor {{fill: #f85149;}}
.cc {{fill: #616e7f;}}
text, tspan {{white-space: pre;}}
</style>
<rect width="{width}px" height="{height}px" fill="{bg_color}" rx="15"/>
<text x="{x_offset_ascii}" y="{y_start_ascii}" fill="{text_color}" class="ascii" font-size="12px">
'''
    for i, line in enumerate(lines):
        # XML escape the line (just in case, but ascii here is safe except maybe ampersands/brackets)
        line = line.replace('<', '&lt;').replace('>', '&gt;').replace('&', '&amp;')
        svg += f'<tspan x="{x_offset_ascii}" y="{y_start_ascii + i * 14}">{line}</tspan>\n'
    svg += '</text>\n'

    # Add the info box on the right
    svg += f'''<text x="{x_offset_info}" y="50" fill="{text_color}">
<tspan x="{x_offset_info}" y="50">taweeporn@maneesin -———————————————————————————————————————————-—-</tspan>
<tspan x="{x_offset_info}" y="80" class="cc">. </tspan><tspan class="key">OS</tspan>:<tspan class="cc"> .............................. </tspan><tspan class="value">Windows 11, IOS, LINUX, ROS</tspan>
<tspan x="{x_offset_info}" y="100" class="cc">. </tspan><tspan class="key">UPtime</tspan>:<tspan class="cc" id="age_data_dots"> .......................... </tspan><tspan class="value" id="age_data">25years 2 months 1 day</tspan>
<tspan x="{x_offset_info}" y="120" class="cc">. </tspan><tspan class="key">Host</tspan>:<tspan class="cc"> ............................ </tspan><tspan class="value">Next Robotics Lab Co. Ltd</tspan>
<tspan x="{x_offset_info}" y="140" class="cc">. </tspan><tspan class="key">Kernel</tspan>:<tspan class="cc"> .......................... </tspan><tspan class="value">Robotics software engineer</tspan>
<tspan x="{x_offset_info}" y="160" class="cc">. </tspan><tspan class="key">IDE</tspan>:<tspan class="cc"> ............................. </tspan><tspan class="value">VSCode, AntigravityIDE</tspan>
<tspan x="{x_offset_info}" y="180" class="cc">. </tspan>
<tspan x="{x_offset_info}" y="200" class="cc">. </tspan><tspan class="key">Languages</tspan>.<tspan class="key">Programming</tspan>:<tspan class="cc"> ........... </tspan><tspan class="value">C++, Python, Javascripts</tspan>
<tspan x="{x_offset_info}" y="220" class="cc">. </tspan><tspan class="key">Languages</tspan>.<tspan class="key">Computer</tspan>:<tspan class="cc"> .............. </tspan><tspan class="value">Vue, html, JSON, YAML</tspan>
<tspan x="{x_offset_info}" y="240" class="cc">. </tspan><tspan class="key">Languages</tspan>.<tspan class="key">Real</tspan>:<tspan class="cc"> .................. </tspan><tspan class="value">English, Thai</tspan>
<tspan x="{x_offset_info}" y="260" class="cc">. </tspan>
<tspan x="{x_offset_info}" y="280" class="cc">. </tspan><tspan class="key">Hobbies</tspan>.<tspan class="key">Software</tspan>:<tspan class="cc"> ................ </tspan><tspan class="value">GAZEBO Simulation, MCU project</tspan>
<tspan x="{x_offset_info}" y="300" class="cc">. </tspan><tspan class="key">Hobbies</tspan>.<tspan class="key">Hardware</tspan>:<tspan class="cc"> ................ </tspan><tspan class="value">3D printer, circuit wiring</tspan>
<tspan x="{x_offset_info}" y="320" class="cc">. </tspan>
<tspan x="{x_offset_info}" y="360">- Contact -————————————————————————————————————————————————————————-—-</tspan>
<tspan x="{x_offset_info}" y="390" class="cc">. </tspan><tspan class="key">Email</tspan>.<tspan class="key">Personal</tspan>:<tspan class="cc"> .................. </tspan><tspan class="value">taweeporn1947@gmail.com</tspan>
<tspan x="{x_offset_info}" y="410" class="cc">. </tspan><tspan class="key">Email</tspan>.<tspan class="key">Personal</tspan>:<tspan class="cc"> .................. </tspan><tspan class="value">taweeporn.m@gmail.com</tspan>
<tspan x="{x_offset_info}" y="430" class="cc">. </tspan><tspan class="key">Email</tspan>.<tspan class="key">Work</tspan>:<tspan class="cc"> ...................... </tspan><tspan class="value">taweeporn.mn@nextroboticslab.com</tspan>
<tspan x="{x_offset_info}" y="450" class="cc">. </tspan><tspan class="key">LinkedIn</tspan>:<tspan class="cc"> ........................ </tspan><tspan class="value">Taweeporn Maneesin</tspan>
<tspan x="{x_offset_info}" y="470" class="cc">. </tspan><tspan class="key">Instagram</tspan>:<tspan class="cc"> ....................... </tspan><tspan class="value">peterdrummer_</tspan>
<tspan x="{x_offset_info}" y="510">- GitHub -————————————————————————————————————————————————————————-—-</tspan>
<tspan x="{x_offset_info}" y="540" class="cc">. </tspan><tspan class="key">Commits</tspan>:<tspan class="cc" id="commit_data_dots"> ......................... </tspan><tspan class="value" id="commit_data">0</tspan>
<tspan x="{x_offset_info}" y="560" class="cc">. </tspan><tspan class="key">Stars</tspan>:<tspan class="cc" id="star_data_dots"> ........................... </tspan><tspan class="value" id="star_data">0</tspan>
<tspan x="{x_offset_info}" y="580" class="cc">. </tspan><tspan class="key">Repositories</tspan>:<tspan class="cc" id="repo_data_dots"> .................... </tspan><tspan class="value" id="repo_data">0</tspan>  <tspan class="cc">(</tspan><tspan class="value" id="contrib_data">0</tspan> <tspan class="cc">contributed)</tspan>
<tspan x="{x_offset_info}" y="600" class="cc">. </tspan><tspan class="key">Followers</tspan>:<tspan class="cc" id="follower_data_dots"> ....................... </tspan><tspan class="value" id="follower_data">0</tspan>
<tspan x="{x_offset_info}" y="620" class="cc">. </tspan><tspan class="key">Lines of Code</tspan>:<tspan class="cc" id="loc_data_dots"> ................... </tspan><tspan class="value" id="loc_data">0</tspan>  <tspan class="cc">(</tspan><tspan class="addColor" id="loc_add">0</tspan> <tspan class="cc">++ / </tspan><tspan class="delColor" id="loc_del">0</tspan> <tspan class="cc">--)</tspan>
</text>
</svg>
'''
    return svg

with open('dark_mode.svg', 'w', encoding='utf-8') as f:
    f.write(make_svg(dark=True))
with open('light_mode.svg', 'w', encoding='utf-8') as f:
    f.write(make_svg(dark=False))
