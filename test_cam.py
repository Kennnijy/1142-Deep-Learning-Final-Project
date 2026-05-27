import cv2

def test_all_cameras():
    print("正在測試編號 0 到 5 的攝影機...")
    
    for index in range(6):
        # cv2.CAP_DSHOW 可以在 Windows 系統下加快偵測速度
        cap = cv2.VideoCapture(index, cv2.CAP_DSHOW)
        
        if cap.isOpened():
            width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
            height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
            print(f"測試中：編號 {index} 可以開啟，解析度為 {int(width)}x{int(height)}")
            print(f"請看彈出的視窗，確認是不是 Iriun 畫面。確認後按任意鍵關閉該視窗。")
            
            # 讀取幾幀畫面確保影像流穩定
            for _ in range(10):
                ret, frame = cap.read()
                
            if ret:
                # 彈出視窗顯示該編號的畫面
                window_name = f"Camera Index: {index}"
                cv2.imshow(window_name, frame)
                cv2.waitKey(0)  # 等待你按下鍵盤任意鍵
                cv2.destroyWindow(window_name)
            
            cap.release()
        else:
            print(f"編號 {index}：無法開啟或不存在")

    print("\n測試結束！")

if __name__ == "__main__":
    test_all_cameras()
