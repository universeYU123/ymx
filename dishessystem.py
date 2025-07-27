class RestaurantOrderSystem:
    def __init__(self):
        # 主要数据结构：菜单字典，存储菜名和价格
        self.menu = {
            "蒜泥空心菜": 30,
            "麻婆豆腐": 20,
            "水煮肉片": 35,
            "小炒黄牛肉": 40,
            "可口可乐": 5,
            "红烧肉": 38,
            "辣椒炒肉": 32,
            "香辣土豆丝": 18,
            "鸡蛋羹": 15,
            "白米饭": 3
        }

        # 用户点菜清单字典，存储菜名和数量
        self.order_list = {}

    def display_menu(self):
        """显示饭店所有菜单"""
        print("=" * 50)
        print("🍽️  欢迎来到美味餐厅  🍽️")
        print("=" * 50)
        print("本饭店的菜单如下：")
        print("-" * 30)
        for i, (dish_name, price) in enumerate(self.menu.items(), 1):
            print(f"{i}. {dish_name:<10} 价格: {price}元")
        print("-" * 30)

    def order_dishes(self):
        """用户点菜功能"""
        while True:
            dish_name = input("\n请输入您要点的菜名（输入'返回'回到主菜单）: ").strip()

            if dish_name == '返回':
                break

            if dish_name not in self.menu:
                print("❌ 抱歉，本店没有这道菜，请重新选择！")
                continue

            try:
                quantity = int(input(f"请输入{dish_name}的数量: "))
                if quantity <= 0:
                    print("❌ 数量必须大于0！")
                    continue

                # 如果菜品已在订单中，则累加数量
                if dish_name in self.order_list:
                    self.order_list[dish_name] += quantity
                    print(f"✅ 已将{dish_name}增加{quantity}份，当前总数: {self.order_list[dish_name]}份")
                else:
                    self.order_list[dish_name] = quantity
                    print(f"✅ 成功添加{dish_name} {quantity}份到订单")

            except ValueError:
                print("❌ 请输入有效的数字！")

    def back_dishes(self):
        """用户退菜功能"""
        if not self.order_list:
            print("❌ 您还没有点任何菜品，无法退菜！")
            return

        print("\n当前已点菜品：")
        for dish_name, quantity in self.order_list.items():
            print(f"- {dish_name}: {quantity}份")

        while True:
            dish_name = input("\n请输入要退的菜名（输入'返回'回到主菜单）: ").strip()

            if dish_name == '返回':
                break

            if dish_name not in self.order_list:
                print("❌ 您没有点这道菜，无法退菜！")
                continue

            try:
                quantity = int(input(f"请输入要退的{dish_name}数量（当前有{self.order_list[dish_name]}份）: "))

                if quantity <= 0:
                    print("❌ 退菜数量必须大于0！")
                    continue

                if quantity > self.order_list[dish_name]:
                    print(f"❌ 退菜数量不能超过已点数量({self.order_list[dish_name]}份)！")
                    continue

                self.order_list[dish_name] -= quantity

                if self.order_list[dish_name] == 0:
                    del self.order_list[dish_name]
                    print(f"✅ 已成功退掉{dish_name} {quantity}份（该菜品已从订单中移除）")
                else:
                    print(f"✅ 已成功退掉{dish_name} {quantity}份，剩余: {self.order_list[dish_name]}份")

            except ValueError:
                print("❌ 请输入有效的数字！")

    def sum_dishes(self):
        """结账功能"""
        if not self.order_list:
            print("❌ 您还没有点任何菜品，无法结账！")
            return

        print("\n" + "=" * 60)
        print("📋               您的订单详情               📋")
        print("=" * 60)

        total_amount = 0

        print(f"{'菜名':<15} {'单价':<10} {'数量':<10} {'小计':<10}")
        print("-" * 60)

        for dish_name, quantity in self.order_list.items():
            unit_price = self.menu[dish_name]
            subtotal = unit_price * quantity
            total_amount += subtotal
            print(f"{dish_name:<15} {unit_price:<10}元 {quantity:<10}份 {subtotal:<10}元")

        print("-" * 60)
        print(f"{'总计金额:':<35} {total_amount}元")

        while True:
            try:
                discount = float(input("\n请输入折扣率（如8.5折请输入0.85，无折扣请输入1）: "))

                if discount <= 0 or discount > 1:
                    print("❌ 折扣率应在0-1之间！")
                    continue

                final_amount = total_amount * discount
                discount_amount = total_amount - final_amount

                print("\n" + "=" * 60)
                print("💰               结账信息               💰")
                print("=" * 60)
                print(f"原价金额: {total_amount:.2f}元")
                print(f"折扣率: {discount * 100:.1f}%")
                print(f"优惠金额: {discount_amount:.2f}元")
                print(f"实付金额: {final_amount:.2f}元")
                print("=" * 60)
                print("谢谢惠顾，欢迎下次光临！🎉")

                # 结账后清空订单
                self.order_list.clear()
                break

            except ValueError:
                print("❌ 请输入有效的数字！")

    def display_current_order(self):
        """显示当前订单"""
        if not self.order_list:
            print("📝 当前订单为空")
            return

        print("\n" + "=" * 40)
        print("📝 当前订单:")
        print("=" * 40)
        for dish_name, quantity in self.order_list.items():
            unit_price = self.menu[dish_name]
            subtotal = unit_price * quantity
            print(f"{dish_name}: {quantity}份 × {unit_price}元 = {subtotal}元")
        print("=" * 40)

    def run(self):
        """主程序运行"""
        print("🎊 欢迎使用餐厅点菜系统 🎊")

        while True:
            # 显示菜单
            self.display_menu()

            # 显示当前订单
            self.display_current_order()

            # 显示功能选择
            print("\n" + "=" * 50)
            print("请选择您要进行的操作：")
            print("1. 查看菜单")
            print("2. 进行点菜")
            print("3. 进行退菜")
            print("4. 显示账单")
            print("5. 退出系统")
            print("=" * 50)

            choice = input("请输入您的选择（1-5）: ").strip()

            if choice == '1':
                # 菜单已在上方显示，这里只需暂停
                input("\n按回车键继续...")

            elif choice == '2':
                self.order_dishes()

            elif choice == '3':
                self.back_dishes()

            elif choice == '4':
                self.sum_dishes()

            elif choice == '5':
                print("👋 谢谢使用，再见！")
                break

            else:
                print("❌ 无效选择，请输入1-5之间的数字！")
                input("按回车键继续...")


# 程序入口
if __name__ == "__main__":
    # 创建餐厅点菜系统实例
    restaurant_system = RestaurantOrderSystem()

    # 运行系统
    restaurant_system.run()