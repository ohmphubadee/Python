import re

# read the file into a string
file_name = input("Enter file name: ")

with open(file_name, 'r') as file:
    data = file.read()

# define the new train number
TDN_new_DownLine_start = int(input("TDN SYR006 start number: "))
TDN_new_UpLine_start = int(input("TDN CLA001 start number: "))

TDN_old_DownLine = [4001,4003,4005,4007,4009,4011,4013,4015,4017,4019,4021,4023,4027,4029,4031,4033,4035,4037,4039,4041,4043,4045,4047,4049,4051,4053,4055,4057,4101,4103,4105,4107,4109,4111,4113,4121,4123,4125,4127,4129,4131,4133,4145,4201,4203,4205,4207,4209,4211,4213,4215,4217,4219,4221,4223,4225,4227,4229,4231,4233,4235,4237,4239,4241,4243,4245,4247,4249,4601,4603,4605,4607,4609,4611,4613,4615,4617,4619,4621,4623,4625,4627,4629,4631,4633,4635,4637,4639,4641,4645,4647,4649,4651,4653,4655,4657,4659,4661,4663,4665,4667,4669,4671,4673,4675,4691,4693,4695,4701,4705,4707,4709,4729,4731,4733,4735,4737,4739,4741,4743,4745,4747,4749,4751,4753,4755,4757,4759,4761,4763,4765,4767,4769,4771,4773,4775,4777,4779,4781,4783,4785,4787,4789,4791,4793,8401,8403,8405,8407,8409,8411,8415,8417,8419,8421,8423,8425,8429,8431,8461,8465,8469,8591,9344,9348,9475
]

TDN_old_Upline =[4012,4014,4016,4018,4020,4022,4024,4026,4028,4030,4032,4034,4036,4038,4040,4044,4046,4048,4050,4052,4054,4056,4058,4060,4062,4064,4066,4068,4070,4072,4074,4076,4080,4082,4084,4086,4088,4090,4092,4094,4170,4172,4174,4202,4204,4206,4208,4210,4212,4214,4216,4218,4220,4222,4224,4226,4228,4234,4236,4238,4240,4242,4244,4246,4248,4600,4602,4604,4606,4608,4610,4612,4614,4616,4618,4622,4624,4626,4628,4630,4632,4634,4636,4638,4640,4642,4646,4648,4650,4652,4654,4656,4658,4660,4662,4664,4666,4668,4670,4672,4674,4676,4678,4680,4682,4684,4686,4688,4720,4722,4724,4726,4730,4732,4734,4736,4738,4740,4742,4744,4746,4748,4750,4752,4754,4756,4758,4760,4762,4764,4768,4770,4772,4774,4776,4778,4780,4782,4784,4786,4788,4790,4792,4794,4796,7516,7518,8400,8402,8404,8406,8408,8412,8414,8416,8418,8420,8422,8426,8428,8430,8434,8436,8460,8464,8494,8592,9343,9347,9476
]

date = f"{file_name[0:10]}/"

#replace version plus 1
version = int(re.search(r'version="(\d+)"',data).group(1))
data = re.sub(r'version="(\d+)"',f'version="{version+1}"',data)


def replace_TDN(TDN_old,TDN_new,date,data):
    
    for TDN in TDN_old:
        pattern_TDN = f'trainNumber="{TDN}"'
        pattern_id = f'id="{date}{TDN}"'
        pattern_ref = f'ref="{date}{TDN}"'
        
        # use regular expression to find the old train number
        # replace the old train number with the new train number

        new_id = f'id="{date}{TDN_new}"'
        new_ref = f'ref="{date}{TDN_new}"'
        new_TDN = f'trainNumber="{TDN_new}"'
        old_id = f'processStatus="planned" id="{date}{TDN}"'
        data = re.sub(pattern_TDN,new_TDN, data)
        data = re.sub(pattern_id, new_id, data)
        data = re.sub(pattern_ref,new_ref,data)
        data = re.sub(f'processStatus="planned" id="{date}{TDN_new}"',old_id,data)
        TDN_new += 1

    return data

data = replace_TDN(TDN_old_DownLine,TDN_new_DownLine_start,date,data)
data = replace_TDN(TDN_old_Upline,TDN_new_UpLine_start,date,data)

# write the updated string back to the file
with open(f'{date[0:10]}_ats_new.xml', 'w') as file:
    file.write(data)

