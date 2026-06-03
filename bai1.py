vehicles = []
datetime = __import__('datetime').datetime
while True :
    print('''
==============================================
       QUẢN LÝ BÃI XE - SMART PARKING
===============================================
    1. Check-in (Đăng ký xe vào)
    2. Báo cáo tồn kho (Hiển thị danh sách)
    3. Tìm kiếm xe (Theo biển số)
    4. Check-out (Xử lý xe ra & Tính phí)
    5. Thoát chương trình
================================================
''')
    choice = int(input("Nhập Lựa chọn của bạn (1-5): ").strip())

    if not choice.isdigit():
        print("Lựa chọn không hợp lệ, vui lòng nhập số từ 1 đến 5.")
        continue
    choice = int(choice)
    if choice not in range(1, 6):
        print("Lựa chọn không hợp lệ, vui lòng nhập số từ 1 đến 5.")
        continue

    match choice:
        case 1:
            plate = input("Nhập biển số xe: ").strip()
            vehicle_type = input("Nhập loại xe (xe máy, ô tô): ").strip().lower()
            if any(vehicle["plate"] == plate for vehicle in vehicles):
                print("Lỗi! Biển số đã tồn tại trong bãi xe.")
                continue
            if vehicle_type not in ["xe máy", "ô tô"]:
                print("Lỗi! Loại xe không hợp lệ. Vui lòng nhập 'xe máy' hoặc 'ô tô'.")
                continue
            new_vehicle = {
                "id": len(vehicles) + 1,
                "plate": plate,
                "type": vehicle_type,
                "check_in_time": datetime.now()
            }
            vehicles.append(new_vehicle)
            print("Đã đăng ký xe vào bãi thành công.")
        
        case 3:
            if not vehicles:
                print("ERR-01: Bãi xe hiện đang trống.")
            else:
                search_plate = input("Nhập biển số xe cần tìm: ").strip()

                found_vehicle = None

                for vehicle in vehicles:
                    if vehicle["plate"] == search_plate:
                        found_vehicle = vehicle
                        break

                if found_vehicle is None:
                    print("ERR-04: Không tìm thấy xe trong bãi.")
                else:
                    print("\n--- THÔNG TIN CHI TIẾT ---")
                    print(f"Mã ID     : {found_vehicle['id']}")
                    print(f"Biển số   : {found_vehicle['plate']}")
                    print(f"Loại xe   : {found_vehicle['type']}")
                    print(f"Giờ vào   : {found_vehicle['check_in_time']}")
        
        case 4:
            checkout_plate = input("Nhập biển số xe cần Check-out: ").strip()

            found_idx = -1

            for i in range(len(vehicles)):
                if vehicles[i]["plate"] == checkout_plate:
                    found_idx = i
                    break

            if found_idx == -1:
                print("ERR-04: Không tìm thấy xe trong bãi.")
            else:
                vehicle = vehicles[found_idx]

                exit_time = datetime.now()

                hours = (exit_time - vehicle["check_in_time"]).total_seconds() / 3600

                if hours < 1:
                    hours = 1

                rate = 5000 if vehicle["type"] == "xe máy" else 15000
                total_fee = int(hours * rate)

                print(f"\nCheck-out thành công xe {checkout_plate}!")
                print(f"Thời gian đỗ: {hours:.2f} giờ.")
                print(f"Tổng phí phải thanh toán: {total_fee:,} VNĐ")

                del vehicles[found_idx]   

        case 5:
            print("Thoát chương trình. Hẹn gặp lại!")
            break
        case _:
            print("Lựa chọn không hợp lệ. Vui lòng nhập số từ 1 đến 5.")