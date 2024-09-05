$exePath = "C:\Program Files\OpenHardwareMonitor\OpenHardwareMonitor.exe"

$process = Start-Process -FilePath $exePath -PassThru
Start-Sleep -Seconds 2
Add-Type @"
    using System;
    using System.Runtime.InteropServices;
    public class WindowControl {
        [DllImport("user32.dll")]
        [return: MarshalAs(UnmanagedType.Bool)]
        public static extern bool ShowWindow(IntPtr hWnd, int nCmdShow);
    }
"@

$WindowHandle = $process.MainWindowHandle
[void][WindowControl]::ShowWindow($WindowHandle, 2)
