#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File     : test.py
# @Author   : jade
# @Date     : 2023/3/10 13:58
# @Email    : jadehh@1ive.com
# @Software : Samples
# @Desc     :
import os
#返回上一层目录
def GetPreviousDir(savepath):

    return os.path.dirname(savepath)

def get_app_name(args):
    return args.app_name

def packSetup(args, exec_path, uuid,output_name=None):
    print("测试使用本地的打包模块")
    file_list = [os.path.join(os.getcwd(),"releases/算法配置客户端V2.0.1.3/Windows/AlgorithmConfiure.exe")]
    if output_name is None:
        output_name =  get_app_name(args) + "_setup-V" + args.app_version[:-2] + "-" + args.app_version[-1]

    issname = "{}.iss".format(output_name)
    with open(issname, 'wb') as f:
        content = "; Script generated by the Inno Setup Script Wizard.\n" \
                  "; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!\n" \
                  "[Setup]\n" \
                  "; NOTE: The value of AppId uniquely identifies this application.\n" \
                  "; Do not use the same AppId value in installers for other applications.\n" \
                  "; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)\n" \
                  "VersionInfoVersion = {}\n" \
                  "AppCopyright = Copyright (C) 2019-{} Samples, Inc.\n" \
                  "AppId={}\n" \
                  ";应用名称\n" \
                  "AppName={}\n" \
                  ";应用版本号\n" \
                  "AppVersion={}\n" \
                  ";AppVerName={}\n" \
                  ";应用发布方\n" \
                  "AppPublisher=南京三宝科技有限公司\n" \
                  ";安装目录名称\n" \
                  "DefaultDirName={}\{}\n" \
                  "DefaultGroupName={}\n" \
                  ";安装目录不可选择\n" \
                  "DisableDirPage=yes\n" \
                  ";安装包文件名\n" \
                  "OutputBaseFilename={}\n" \
                  ";压缩包\n" \
                  "Compression=lzma\n" \
                  "SolidCompression=yes\n" \
                  ";安装包图标文件\n" \
                  "SetupIconFile={}\n" \
                  ";设置控制面板中程序图标\n" \
                  "UninstallDisplayIcon={}\n" \
                  ";设置控制面板中程序的名称\n" \
                  "UninstallDisplayName = {}\n" \
                  ";许可文件\n" \
                  ";LicenseFile=\n" \
                  "[Files]\n" \
                  ";安装文件\n" \
            .format(args.app_version, "2023", uuid, get_app_name(args), args.app_version, args.name,
                    "C:\\", get_app_name(args), get_app_name(args),
                   output_name,
                    os.path.abspath("icons/app_logo.ico"), os.path.abspath("icons/app_logo.ico"), args.name)

        for file in file_list:
            if len(file.split(exec_path)[-1].split("\\")) > 2:
                path = ""
                for p_file in file.split(exec_path)[-1].split("\\")[:-1]:
                    if p_file:
                        path = path + "\\" + p_file
                cmd_str = 'Source: "{}"; DestDir: "{}\\{}"; Flags: ignoreversion\n'.format(file, '{app}', path)
            else:
                cmd_str = 'Source: "{}"; DestDir: "{}\\{}"; Flags: ignoreversion \n'.format(file, '{app}', "")

            content = content + cmd_str
        content_back = ';[Registry]\n' \
                       ';开机启动\n' \
                       ';Root: HKLM; Subkey: "SOFTWARE\Microsoft\Windows\CurrentVersion\Run"; ValueType: string; ValueName: "MES Monitoring Client"; ValueData: """{}\Client\MES-MonitoringClient.exe"""; Flags: uninsdeletevalue\n' \
                       '[Icons]\n' \
                       'Name: "{}\{}"; Filename: "{}\{}"\n' \
                       'Name: "{}\{}"; Filename: "{}\{}"; Tasks: desktopicon;\n' \
                       '[Tasks]\n' \
                       'Name: "desktopicon"; Description: "{}"; GroupDescription: "{}"; Flags: checkablealone\n' \
                       '[run]\n' \
                       ';两种方法都可以安装服务，上面的可以将服务安装好，但不能直接运行\n' \
                       ';以下的方式可以直接运行，其中有Components:Service;当选中了服务才会安装服务\n' \
                       ';Flags:postinstall点击完成后，才会进行服务的安装，因为在处理RabbitMQ的服务器参数时，不会直接替换参数的\n' \
                       ';安装完成后启动应用\n' \
                       'Filename: "{}\{}"; Description: "{}";Flags:postinstall nowait skipifsilent \n' \
                       '[UninstallRun]\n' \
                       ';卸载时，停止服务并删除服务\n' \
                       ';Filename:{}\sc.exe; Parameters: "stop MESUploadDataService" ; Flags: runhidden; Components:Service\n' \
                       ';Filename: {}\sc.exe; Parameters: "delete MESUploadDataService" ; Flags: runhidden; Components:Service\n' \
                       '[Messages]\n' \
                       ';安装时，windows任务栏提示标题\n' \
                       'SetupAppTitle={}\n' \
                       ';安装时，安装引导标题\n' \
                       'SetupWindowTitle={}\n' \
                       ';在界面左下角加文字\n' \
                       'BeveledLabel=南京三宝科技有限公司\n' \
                       ';卸载对话框说明\n' \
                       'ConfirmUninstall=您真的想要从电脑中卸载 %1 吗?%n%n按 [是] 则完全删除 %1 以及它的所有组件;%n按 [否]则让软件继续留在您的电脑上.\n' \
                       ';[Types]\n' \
                       ';Name: "normaltype"; Description: "Normal Setup"\n' \
                       ';Name: "custom";     Description: "Custom Installation"; Flags: iscustom\n' \
                       ';[Components]\n' \
                       ';Name: "Client";     Description: "应用界面";  Types: normaltype custom\n' \
                       '[Code]\n' \
                       '//设置界面文字颜色\n' \
                       'procedure InitializeWizard();\n' \
                       'begin\n' \
                       '//WizardForm.WELCOMELABEL1.Font.Color:= clGreen;//设置开始安装页面第一段文字的颜色为绿色\n' \
                       '//WizardForm.WELCOMELABEL2.Font.Color:= clOlive;//设置开始安装页面第二段文字的颜色为橄榄绿\n' \
                       '//WizardForm.PAGENAMELABEL.Font.Color:= clRed;//设置许可协议页面第一段文字的颜色为红色\n' \
                       '//WizardForm.PAGEDESCRIPTIONLABEL.Font.Color:= clBlue; //设置许可协议页面第二段文字的颜色为蓝色\n' \
                       'WizardForm.MainPanel.Color:= clWhite;//设置窗格的颜色为白色\n' \
                       'end;\n' \
                       '//卸载后打开网址\n' \
                       '//procedure CurUninstallStepChanged(CurUninstallStep: TUninstallStep);\n' \
                       '//var\n' \
                       '//  ErrorCode: Integer;\n' \
                       '//begin\n' \
                       '//  case CurUninstallStep of\n' \
                       '//   usUninstall:\n' \
                       '//     begin\n' \
                       '// 正在卸载\n' \
                       '//    end;\n' \
                       '//  usPostUninstall:\n' \
                       '//    begin\n' \
            .format("{app}",
                    "{group}", args.name, "{app}", get_app_name(args) + ".exe",
                    "{commondesktop}", args.name, "{app}", get_app_name(args) + ".exe",
                    "{cm:CreateDesktopIcon}", "{cm:AdditionalIcons}",
                    "{app}", get_app_name(args) + ".exe", "{" + "cm:LaunchProgram,{}".format(args.name) + "}",
                    "{sys}", "{sys}",
                    args.name + "-安装", args.name + "-安装")
        content = content + content_back
        content_code = "[Code]\n" \
                       "//;通过名称终结进程\n" \
                       "// 自定义函数，判断软件是否运行，参数为需要判断的软件的exe名称\n" \
                       "procedure CheckSoftRun(strExeName: String);\n" \
                       "// 变量定义\n" \
                       "var ErrorCode: Integer;\n" \
                       "var strCmdKill: String;  // 终止软件命令\n" \
                       "begin\n" \
                       "strCmdKill := Format('/c taskkill /f /t /im %s', [strExeName]);\n" \
                       "// 终止程序\n" \
                       "ShellExec('open', ExpandConstant('{}'), strCmdKill, '', SW_HIDE, ewNoWait, ErrorCode);\n" \
                       "end;\n" \
                       "function InitializeSetup(): Boolean;\n" \
                       "begin\n" \
                       " CheckSoftRun('{}');\n" \
                       "if (DirExists('{}\\{}')) then\n" \
                       "begin\n" \
                       "if MsgBox('是否要卸载旧版程序？', mbConfirmation, MB_YESNO) = IDYES then\n" \
                       "begin\n" \
                       "//删除文件夹及其中所有文件\n" \
                       "DelTree('{}\\{}', True, True, True);\n" \
                       "Result := True;\n" \
                       "end\n" \
                       "else\n" \
                       "begin\n" \
                       "Result := False;\n" \
                       "end;\n" \
                       "end\n" \
                       "else\n" \
                       "begin\n" \
                       "Result := True;\n" \
                       "end;\n" \
                       "end;\n".format("{cmd}", get_app_name(args) + ".exe", "C:", get_app_name(args), "C:",
                                       get_app_name(args))
        content = content + content_code
        print(content)
        f.write(content.encode("gbk"))
    inno_setup_path = os.path.join(GetPreviousDir(os.getcwd()), "InnoSetup")
    if os.path.exists(inno_setup_path):
        print("Inno Setup Path exists,dir:{}".format(inno_setup_path))
        cmd_str = "{} {}".format(os.path.join(inno_setup_path, "ISCC.exe"), os.path.join(os.getcwd(), issname))
        print("cmd str:{}".format(cmd_str))
        os.system(cmd_str)
        #subprocess.run(cmd_str, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        #os.remove(os.path.join(os.getcwd(), issname))
def test_inno_setup():
    import argparse
    lib_path = "algorithm_configure_lib32"
    parser = argparse.ArgumentParser()
    parser.add_argument('--extra_sys_list', type=str,
                        default="")  ## 需要额外打包的路径
    parser.add_argument('--scripts_path', type=str,
                        default="")  ## 打包成一个完成的包
    parser.add_argument('--full', type=str,
                        default="False")  ## 打包成一个完成的包
    parser.add_argument('--extra_path_list', type=list,
                        default=["qss", ("data", "xpinyin"), "resources", "translator", "fonts", "bin",
                                 ("lib/Linux", "lib/Linux"),
                                 ("lib/Windows/api-ms-win-crt-process-l1-1-0.dll", ".")])

    parser.add_argument('--lib_path', type=str, default=lib_path)  ## 是否lib包分开打包
    parser.add_argument("--head_str", type=str, default="from jade import *\n"
                                                        "update_lib('/tmp/{}')\n".format(lib_path))
    parser.add_argument('--use_jade_log', type=str,
                        default="True")  ##是否使用JadeLog

    parser.add_argument('--console', type=str,
                        default="False")  ## 是否显示命令行窗口,只针对与Windows有效
    parser.add_argument("--app_version", type=str, default="2.0.1.3")  ## 版本号
    parser.add_argument('--app_name', type=str,
                        default="AlgorithmConfiure")  ##需要打包的文件名称
    parser.add_argument('--name', type=str,
                            default="算法配置客户端")  ##需要打包的文件名称
    parser.add_argument('--appimage', type=str,
                        default="True")  ## 是否打包成AppImage

    parser.add_argument('--is_qt', type=str, default="True")  ## qt 会将controller view src 都进行编译
    parser.add_argument('--specify_files', type=str, default="")  ## 指定编译的文件
    args = parser.parse_args()

    install_path = os.path.join(os.getcwd(),
                                    "releases/{}/{}".format(args.name + "V" + args.app_version, "Windows"))

    packSetup(args,install_path, "{{05b64abe-0e24-11ed-b3da-005056c00009}", "test")

    file_list = os.listdir("Output")
    print(file_list)


def test_print_chinese():
    import sys
    print("sys.stdout.encoding:{}".format(sys.stdout.encoding))
    print("中文输出")
if __name__ == '__main__':
    test_inno_setup()