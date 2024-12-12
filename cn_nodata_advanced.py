import requests
import asyncio
import datetime
from telegram import Bot
from telegram.error import TelegramError

# Variable for Conectivity
api_url = "http://172.30.0.16/api/v1/datapoints/query"
bot_token = "7143675059:AAFLMaLYEP9fl4nqwYfUQSpYfSQ-QgKNwYk"
chat_id = "-4169772122"

# Variable that been used for gathering the Data
gateway = ('GW01-BTM_Beacon', "GW02-CKR_Beacon", 'GW03-PTK_Beacon', 'GW04-BJM_Beacon', 'GW05-TAR_Beacon', 'GW06-MND_Beacon', 'GW07-KPG_Beacon', 'GW08-AMB_Beacon', 'GW09-MNK_Beacon', 'GW10-TIM_Beacon', 'GW11-JAP_Beacon')
iteration_gw = {gw_location : [0] for gw_location in ('GW01-BTM_Beacon', "GW02-CKR_Beacon", 'GW03-PTK_Beacon', 'GW04-BJM_Beacon', 'GW05-TAR_Beacon', 'GW06-MND_Beacon', 'GW07-KPG_Beacon', 'GW08-AMB_Beacon', 'GW09-MNK_Beacon', 'GW10-TIM_Beacon', 'GW11-JAP_Beacon')}
reference = ['Beam_1_OR_1', 'Beam_3_OR_1', 'Beam_4U_OR_1', 'Beam_4L_OR_1', 'Beam_5U_OR_1', 'Beam_5L_OR_1', 'Beam_6U_OR_1', 'Beam_6L_OR_1', 'Beam_7U_OR_1', 'Beam_7L_OR_1', 'Beam_8U_OR_1', 'Beam_8L_OR_1', 'Beam_9_OR_1', 'Beam_10_OR_1', 'Beam_11_OR_1', 'Beam_12U_OR_1', 'Beam_12L_OR_1', 'Beam_13U_OR_1', 'Beam_13L_OR_1', 'Beam_14U_OR_1', 'Beam_14L_OR_1', 'Beam_15U_OR_1', 'Beam_15L_OR_1', 'Beam_16_OR_1', 'Beam_17U_OR_1', 'Beam_17L_OR_1', 'Beam_18_OR_1', 'Beam_19U_OR_1', 'Beam_19L_OR_1', 'Beam_20_OR_1', 'Beam_21_OR_1', 'Beam_22_OR_1', 'Beam_23_OR_1', 'Beam_24_OR_1', 'Beam_25_OR_1', 'Beam_26_OR_1', 'Beam_27_OR_1', 'Beam_28U_OR_1', 'Beam_28L_OR_1', 'Beam_30_OR_1', 'Beam_31_OR_1', 'Beam_32_OR_1', 'Beam_33_OR_1', 'Beam_34_OR_1', 'Beam_35_OR_1', 'Beam_36_OR_1', 'Beam_37U_OR_1', 'Beam_37L_OR_1', 'Beam_38_OR_1', 'Beam_39_OR_1', 'Beam_40_OR_1', 'Beam_41_OR_1', 'Beam_42_OR_1', 'Beam_43_OR_1', 'Beam_44_OR_1', 'Beam_45_OR_1', 'Beam_46_OR_1', 'Beam_47_OR_1', 'Beam_48_OR_1', 'Beam_49_OR_1', 'Beam_50_OR_1', 'Beam_51_OR_1', 'Beam_52_OR_1', 'Beam_53_OR_1', 'Beam_54_OR_1', 'Beam_55_OR_1', 'Beam_56_OR_1', 'Beam_57_OR_1', 'Beam_58_OR_1', 'Beam_59U_OR_1', 'Beam_59L_OR_1', 'Beam_60U_OR_1', 'Beam_60L_OR_1', 'Beam_61_OR_1', 'Beam_62_OR_1', 'Beam_63_OR_1', 'Beam_64_OR_1', 'Beam_65_OR_1', 'Beam_66_OR_1', 'Beam_67_OR_1', 'Beam_68_OR_1', 'Beam_69U_OR_1', 'Beam_69L_OR_1', 'Beam_70_OR_1', 'Beam_71_OR_1', 'Beam_72_OR_1', 'Beam_73_OR_1', 'Beam_74_OR_1', 'Beam_75_OR_1', 'Beam_76_OR_1', 'Beam_77_OR_1', 'Beam_78_OR_1', 'Beam_79_OR_1', 'Beam_80_OR_1', 'Beam_81_OR_1', 'Beam_82_OR_1', 'Beam_83_OR_1', 'Beam_84_OR_1', 'Beam_85_OR_1', 'Beam_86_OR_1', 'Beam_87_OR_1', 'Beam_88_OR_1', 'Beam_89_OR_1', 'Beam_90_OR_1', 'Beam_91_OR_1', 'Beam_92_OR_1', 'Beam_93_OR_1', 'Beam_94_OR_1', 'Beam_95_OR_1', 'Beam_96_OR_1', 'Beam_97_OR_1', 'Beam_98_OR_1', 'Beam_99_OR_1', 'Beam_100_OR_1', 'Beam_101_OR_1', 'Beam_102_OR_1', 'Beam_103_OR_1', 'Beam_104_OR_1', 'Beam_105_OR_1']
all_numbers = ['Beam-1', 'Beam-3', 'Beam-4U', 'Beam-4L', 'Beam-5U', 'Beam-5L', 'Beam-6U', 'Beam-6L', 'Beam-7U', 'Beam-7L', 'Beam-8U', 'Beam-8L', 'Beam-9', 'Beam-10', 'Beam-11', 'Beam-12U', 'Beam-12L', 'Beam-13U', 'Beam-13L', 'Beam-14U', 'Beam-14L', 'Beam-15U', 'Beam-15L', 'Beam-16', 'Beam-17U', 'Beam-17L', 'Beam-18', 'Beam-19U', 'Beam-19L', 'Beam-20', 'Beam-21', 'Beam-22', 'Beam-23', 'Beam-24', 'Beam-25', 'Beam-26', 'Beam-27', 'Beam-28U', 'Beam-28L', 'Beam-30', 'Beam-31', 'Beam-32', 'Beam-33', 'Beam-34', 'Beam-35', 'Beam-36', 'Beam-37U', 'Beam-37L', 'Beam-38', 'Beam-39', 'Beam-40', 'Beam-41', 'Beam-42', 'Beam-43', 'Beam-44', 'Beam-45', 'Beam-46', 'Beam-47', 'Beam-48', 'Beam-49', 'Beam-50', 'Beam-51', 'Beam-52', 'Beam-53', 'Beam-54', 'Beam-55', 'Beam-56', 'Beam-57', 'Beam-58', 'Beam-59U', 'Beam-59L', 'Beam-60U', 'Beam-60L', 'Beam-61', 'Beam-62', 'Beam-63', 'Beam-64', 'Beam-65', 'Beam-66', 'Beam-67', 'Beam-68', 'Beam-69U', 'Beam-69L', 'Beam-70', 'Beam-71', 'Beam-72', 'Beam-73', 'Beam-74', 'Beam-75', 'Beam-76', 'Beam-77', 'Beam-78', 'Beam-79', 'Beam-80', 'Beam-81', 'Beam-82', 'Beam-83', 'Beam-84', 'Beam-85', 'Beam-86', 'Beam-87', 'Beam-88', 'Beam-89', 'Beam-90', 'Beam-91', 'Beam-92', 'Beam-93', 'Beam-94', 'Beam-95', 'Beam-96', 'Beam-97', 'Beam-98', 'Beam-99', 'Beam-100', 'Beam-101', 'Beam-102', 'Beam-103', 'Beam-104', 'Beam-105']
iteration_beam = {site_or : [0] for site_or in ('Beam_1_OR_1',	'Beam_3_OR_1',	'Beam_4U_OR_1',	'Beam_4L_OR_1',	'Beam_5U_OR_1',	'Beam_5L_OR_1',	'Beam_6U_OR_1',	'Beam_6L_OR_1',	'Beam_7U_OR_1',	'Beam_7L_OR_1',	'Beam_8U_OR_1',	'Beam_8L_OR_1',	'Beam_9_OR_1',	'Beam_10_OR_1',	'Beam_11_OR_1',	'Beam_12U_OR_1',	'Beam_12L_OR_1',	'Beam_13U_OR_1',	'Beam_13L_OR_1',	'Beam_14U_OR_1',	'Beam_14L_OR_1',	'Beam_15U_OR_1',	'Beam_15L_OR_1',	'Beam_16_OR_1',	'Beam_17U_OR_1',	'Beam_17L_OR_1',	'Beam_18_OR_1',	'Beam_19U_OR_1',	'Beam_19L_OR_1',	'Beam_20_OR_1',	'Beam_21_OR_1',	'Beam_22_OR_1',	'Beam_23_OR_1',	'Beam_24_OR_1',	'Beam_25_OR_1',	'Beam_26_OR_1',	'Beam_27_OR_1',	'Beam_28U_OR_1',	'Beam_28L_OR_1',	'Beam_30_OR_1',	'Beam_31_OR_1',	'Beam_32_OR_1',	'Beam_33_OR_1',	'Beam_34_OR_1',	'Beam_35_OR_1',	'Beam_36_OR_1',	'Beam_37U_OR_1',	'Beam_37L_OR_1',	'Beam_38_OR_1',	'Beam_39_OR_1',	'Beam_40_OR_1',	'Beam_41_OR_1',	'Beam_42_OR_1',	'Beam_43_OR_1',	'Beam_44_OR_1',	'Beam_45_OR_1',	'Beam_46_OR_1',	'Beam_47_OR_1',	'Beam_48_OR_1',	'Beam_49_OR_1',	'Beam_50_OR_1',	'Beam_51_OR_1',	'Beam_52_OR_1',	'Beam_53_OR_1',	'Beam_54_OR_1',	'Beam_55_OR_1',	'Beam_56_OR_1',	'Beam_57_OR_1',	'Beam_58_OR_1',	'Beam_59U_OR_1',	'Beam_59L_OR_1',	'Beam_60U_OR_1',	'Beam_60L_OR_1',	'Beam_61_OR_1',	'Beam_62_OR_1',	'Beam_63_OR_1',	'Beam_64_OR_1',	'Beam_65_OR_1',	'Beam_66_OR_1',	'Beam_67_OR_1',	'Beam_68_OR_1',	'Beam_69U_OR_1',	'Beam_69L_OR_1',	'Beam_70_OR_1',	'Beam_71_OR_1',	'Beam_72_OR_1',	'Beam_73_OR_1',	'Beam_74_OR_1',	'Beam_75_OR_1',	'Beam_76_OR_1',	'Beam_77_OR_1',	'Beam_78_OR_1',	'Beam_79_OR_1',	'Beam_80_OR_1',	'Beam_81_OR_1',	'Beam_82_OR_1',	'Beam_83_OR_1',	'Beam_84_OR_1',	'Beam_85_OR_1',	'Beam_86_OR_1',	'Beam_87_OR_1',	'Beam_88_OR_1',	'Beam_89_OR_1',	'Beam_90_OR_1',	'Beam_91_OR_1',	'Beam_92_OR_1',	'Beam_93_OR_1',	'Beam_94_OR_1',	'Beam_95_OR_1',	'Beam_96_OR_1',	'Beam_97_OR_1',	'Beam_98_OR_1',	'Beam_99_OR_1',	'Beam_100_OR_1',	'Beam_101_OR_1',	'Beam_102_OR_1',	'Beam_103_OR_1',	'Beam_104_OR_1',	'Beam_105_OR_1',)}
thresholds_beam =  ['11.5', '11.5', '9.0', '9.0', '10.5', '11.0', '11.5', '12.0', '10.0', '10.5', '11.0', '11.5', '6.5', '13.0', '11.5', '11.5', '11.0', '13.0', '14.0', '12.5', '12.5', '10.5', '10.5', '10.0', '12.0', '11.5', '14.5', '9.0', '6.5', '10.5', '10.0', '10.5', '10.5', '10.0', '12.5', '11.0', '10.5', '9.0', '9.0', '9.8', '15.0', '14.0', '9.0', '12.0', '12.0', '9.0', '12.5', '11.5', '9.5', '12.5', '7.0', '12.5', '9.0', '10.0', '10.5', '11.0', '11.5', '9.5', '11.5', '12.5', '11.0', '9.0', '14.0', '12.4', '11.0', '12.0', '6.0', '10.5', '13.0', '11.5', '12.5', '12.0', '12.5', '10.7', '8.0', '13.0', '11.0', '11.5', '9.5', '10.5', '9.5', '9.5', '10.0', '10.5', '12.0', '11.0', '14.0', '12.5', '10.5', '11.0', '12.0', '14.5', '11.0', '13.0', '14.0', '11.0', '13.0', '12.0', '9.0',"11.5", '13.5', '14.5', '11.5', '12.0', '13.5', '14.0', '13.0', '10.5', '10.0', '7.5', '11.5', '9.5', '11.0', '12.5', '12.0', '11.0', '11.5', '12.5', '11.5']
thresholds_gw = {'39', '41', '42', '39', '39', '39', '44', '43', '41', '45', '28'}
beam_status = {}
gateway_status = {}
cds = {}

async def send_telegram_message(message):
    try:
        bot = Bot(token=bot_token)
        await bot.send_message(chat_id=chat_id, text=message)
    except TelegramError as e:
        print(f"Failed to send Telegram message: {str(e)}")

async def get_data_from_json_query(json_query, api_url):
    headers = {"Content-Type": "application/json"}
    try:
        response = requests.post(api_url, json=json_query, headers=headers)

        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None
    
async def cn_gateway (gw_location) :
    json_query = {
        "start_relative": {
            "value": 5,
            "unit": "minutes"
        },
        "metrics": [
            {
            "name": "cn",
            "tags": {
                "carrier": [
                    gw_location
                ]
            }
            }
        ],
        "safeguard": {
            "group_limit": 100,
            "limit_before_aggregation": 10000000,
            "limit_after_aggregation": 10000
        }
    }
    result_gw = await get_data_from_json_query(json_query, api_url )
    gw_condition = 1
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


    if result_gw is not None:
        values = result_gw['queries'][0]['results'][0]['values']
        timestamp, value = values[-1] if values else (0, None)
        gw_condition = 0
    else :
        values = None
        gw_condition = 1
        value = None
    
    if gw_condition == 1:
        iteration_gw[gw_location][0] += 1
        print(f"⚠️ {gw_location} CN data is None ⚠️")
        if iteration_gw[gw_location][0] == 15 :
            start_time = (datetime.datetime.now() - datetime.timedelta(minutes=20)).strftime('%Y-%m-%d %H:%M:%S')
            gateway_status[gw_location] = {'down' : True, 'start_time' : start_time}
            status = f"❗❗❗ ATTENTION ❗❗❗\n===========\nCN for {gw_location} is None\n\nPLEASE CHECK IT ❗❗❗"
            await send_telegram_message(status)
            print(status)
        else :
            status = f"❗❗❗ ATTENTION ❗❗❗\n===========\nCN for {gw_location} is None\n\nPLEASE CHECK IT ❗❗❗"
            print(status)
    else:
        if value is None:
            iteration_gw[gw_location][0] += 1
            print(f"⚠️ {gw_location} CN is no Data ⚠️")
            cds[gw_location] = {'down' : True}
            if iteration_gw[gw_location][0] == 15 :
                start_time = (datetime.datetime.now() - datetime.timedelta(minutes=20)).strftime('%Y-%m-%d %H:%M:%S')
                gateway_status[gw_location] = {'down' : True, 'start_time' : start_time}
                status = f"❗❗❗ ATTENTION ❗❗❗\n===========\nCN for {gw_location} is no data\n\nPLEASE CHECK IT ❗❗❗"
                await send_telegram_message(status)
                print(status)
        else:
            if gw_location in gateway_status and gateway_status[gw_location] :
                downtime_start_time = datetime.datetime.strptime(gateway_status[gw_location]['start_time'], '%Y-%m-%d %H:%M:%S')
                downtime_duration = datetime.datetime.strptime(current_time, '%Y-%m-%d %H:%M:%S') - downtime_start_time
                gateway_status[gw_location]['down'] = False
                gateway_status[gw_location] = False
                del gateway_status[gw_location]
                del cds[gw_location]
                normal = f"✅ NORMAL ✅\n CN for {gw_location} is Normal at {value}\n\nDown for about {downtime_duration}"
                await send_telegram_message(normal)
                iteration_gw[gw_location][0] = 0
            else :
                if gw_location in cds and cds[gw_location]:
                    del cds[gw_location]
                iteration_gw[gw_location][0] = 0
                status = f"CN for {gw_location} is Normal at {value} dB"
                print(status)
            
    if all(gw_location in cds for gw_location in gateway):
        n+=1 
        if n == 1 :
            CDS = f"❗⚠️❗⚠️ CDS HANG ⚠️❗⚠️❗\n\nCN is Down Please Check it ❗❗❗"
            await send_telegram_message(CDS)
        else :
            pass
    print
    print('=======================\n')

async def cn_reference(rt_name, rt_number):
    json_query = {
        "start_relative": {
            "value": 5,
            "unit": "minutes"
        },
        "metrics": [
            {
                "name": "cn",
                "tags": {
                    "carrier": [
                        rt_name
                    ]
                }
            }
        ],
        "safeguard": {
            "group_limit": 100,
            "limit_before_aggregation": 10000000,
            "limit_after_aggregation": 10000
        }
    }

    result_rt = await get_data_from_json_query(json_query, api_url)
    gw_condition = 1

    if result_rt is not None:
        values = result_rt['queries'][0]['results'][0]['values']
        timestamp, value = values[-1] if values else (0, None)
        gw_condition = 0
    else:
        values = None
        gw_condition = 1
        value = None

    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    if gw_condition == 1:
        iteration_beam[rt_name][0] += 1
        print(f"⚠️⚠️⚠️ {rt_number} CN data is None ⚠️⚠️⚠️")
        if iteration_beam == 10 :
            start_time = (datetime.datetime.now() - datetime.timedelta(minutes=15)).strftime('%Y-%m-%d %H:%M:%S')
            beam_status[rt_name] = {'down' : True, 'start_time' : start_time}
            status = f"⚠️⚠️⚠️ Warning ⚠️⚠️⚠️\n===========\nCN for {rt_number} is None\n\nPlease Check It !!!"
            await send_telegram_message(status)
            print(status)
        else :
            status = f"⚠️⚠️⚠️ Warning ⚠️⚠️⚠️\n===========\nCN for {rt_number} is None\n\nPlease Check It !!!"
            print(status)
    else:
        if value is None:
            iteration_beam[rt_name][0] += 1
            print(f"⚠️⚠️⚠️ {rt_number} CN is no Data ⚠️⚠️⚠️")
            if iteration_beam[rt_name][0] == 10 :
                start_time = (datetime.datetime.now() - datetime.timedelta(minutes=15)).strftime('%Y-%m-%d %H:%M:%S')
                beam_status[rt_name] = {'down' : True, 'start_time' : start_time}
                status = f"⚠️⚠️⚠️ Warning ⚠️⚠️⚠️\n===========\nCN for {rt_number} is no data\n\nPlease Check It !!!"
                await send_telegram_message(status)
                print(status)
        else:
            if rt_name in beam_status and beam_status[rt_name] :
                downtime_start_time = datetime.datetime.strptime(beam_status[rt_name]["start_time"], '%Y-%m-%d %H:%M:%S')
                downtime_duration = datetime.datetime.strptime(current_time, '%Y-%m-%d %H:%M:%S') - downtime_start_time
                beam_status[rt_name]['down'] = False
                beam_status[rt_name] = False
                normal = f"✅ NORMAL ✅\n CN for {rt_number} is Normal at {value}\n\nDown for about {downtime_duration}"
                await send_telegram_message(normal)
                iteration_beam[rt_name][0] = 0
            else :
                iteration_beam[rt_name][0] = 0
                status = f"CN for {rt_number} is Normal at {value} dB"
                print(status)

    print('=======================\n')

# Assume there is a definition for get_data_from_json_query and api_url

async def main():
    while True :
        for lokasi in gateway :
            await cn_gateway(lokasi)
        for location, number in zip(reference, all_numbers) :
            await cn_reference(location, number)
        print("Waiting for a Minutes")
        await asyncio.sleep(60)
asyncio.run(main())