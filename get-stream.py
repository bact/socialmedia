from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

class MyListener(StreamListener):
    def on_data(self, data):
        try:
            with open('stream_common_words.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True

THAI_COMMON_WORDS = [
    'ที่','การ','เป็น','ใน','จะ',
    'มี','ของ','ไม่','และ','ได้',
    'ว่า','ไป','ให้','มา','ก็',
    'คน','ความ','แล้ว','กับ','อยู่',
    'หรือ','กัน','นี้','แต่','จาก',
    'อย่าง','เขา','ต้อง','ด้วย','ขึ้น',
    'นั้น','ผู้','ซึ่ง','ตาม','มาก',
    'โดย','ใช้','เรื่อง','ยัง','ทาง',
    'เรา','ผม','ทำ','อีก','เมื่อ',
    'ฉัน','เข้า','หนึ่ง','เพื่อ','ถึง',
    'เพราะ','ดี','ออก','เห็น','เกิด',
    'คือ','เธอ','จึง','ไว้','ตัว',
    'กว่า','ทำให้','คุณ','เลย','ปี',
    'ไทย','มัน','ทั้ง','อะไร','ถ้า',
    'ต่อ','ลง','เวลา','ส่วน','ต่าง',
    'วัน','ทุก','อาจ','แบบ','ประเทศ',
    'ก่อน','ถูก','ดู','รู้','เอา',
    'อื่น','ครั้ง','เช่น','นะ','สอง',
    'หน้า','นาย','บอก','กลับ','งาน',
    'นำ','แห่ง','จน','บาง','เด็ก',
    'เหมือน','พระ','คิด','นี่','ได้รับ',
    'พูด','บ้าน','สามารถ','เคย','ชีวิต',
    'ด้าน','ใคร','รับ','หลาย','สิ่ง',
    'เสียง','ใหม่','อยาก','คง','หา',
    'มอง','คำ','ปัญหา','สังคม','กลุ่ม',
    'ใช่','ใด','ท่าน','น้ำ','กำลัง',
    'ลูก','ขอ','จริง','แม่','ช่วย',
    'พอ','ระหว่าง','เงิน','เอง','ใหญ่',
    'สำหรับ','โลก','ผล','แสดง','อัน',
    'เดิน','พี่','สร้าง','เสีย','พบ',
    'ทำงาน','สี','น่า','ใจ','กำหนด',
    'เมือง','บน','ที่สุด','แก่','น้อย',
    'มาตรา','กิน','ระบบ','ร่วม','หาก',
    'ควร','พัฒนา','สูง','เดียว','ตัวเอง',
    'แรก','อาหาร','พวก','สาว','ครับ',
    'หลัง','นัก','ฝ่าย','เพื่อน','ถาม',
    'กล่าว','กรณี','ส่ง','เพียง','เริ่ม',
    'ตา','บ้าง','ข้อ','ช่วง','ระดับ',
    'ตน','รัก','เกี่ยวกับ','จัด','ห้อง',
    'ลักษณะ','วันที่','กฎหมาย','ดังกล่าว','อำนาจ',
    'พ่อ','ไหน','หนังสือ','บุคคล','รวม',
    'จำนวน','ตอน','พิจารณา','เรียน','ทรง',
    'ภาพ','ตรง','ยิ่ง','ชอบ','ภาษา',
    'ตั้งแต่','ดัง','ตั้ง','ผ่าน','เข้าใจ',
    'อย่า','ห้าม','ที่ไหน','อย่างไร','ทำไม',
    'เลือก','แค่','นั่น','คะ','ค่ะ',
    'พร้อม','เจ้า','มัก','บ่อย','ติด',
    'ใส่','ละ','ล่ะ','หมด','เพิ่ม',
    'ลด','เท่านั้น','ตาย','เศรษฐกิจ','การเมือง',
    'สำคัญ','รู้สึก','ต่อไป','เปิด','ปิด',
    'ตก','เฉย','เงื่อนไข','ยิ่ง','เกลียด',
    'เบื่อ','เกิน','ค่อน','ค่อย','ซ้ำ',
    'ทั่ว','ง่าย','ยาก','โดน','เล็ก',
    'สบาย','ลำบาก','เครียด','นาน','ช้า',
    'เร็ว','ยาว','สั้น','เปรียบ','เทียบ',
    'หิว','เจอ','จับ','แย่ง','รอ',
    'บริการ','ผอม','อ้วน','แข่ง','เซ็ง',
    'ร้อน','หนาว','เย็น','เข้า','ดึก',
    'ค่ำ','บ่าย','กลาง','คืน','คับ',
    'มือ','ถือ','ขับ','รถ','ถนน',
    'แพง','ราคา','ผ่อน','ขำ','หัว',
    'ท้าย','ปลาย','ต้น','สาย','เส้น',
    'บัตร','ลุ้น','โชค','เสี่ยง','ทุน',
    'ซื้อ','ขาย','ร้าน','แบรนด์','ยี่ห้อ',
    'อิน','โซเชียล','เฟซ','เฟส','โพส',
    'แตก','หัก','พัง','ยับ','เก่า',
    'ซ่อม','ทุบ','เกม','รอด','หาย',
    'ห่วง','โรค','มหา','จบ','ล่าง',
    'สินค้า','จ่าย','เลิก','แพ้','ชนะ',
    'ยอม','ขนาด','ขน','ร้อง','เสียบ',
    'สมัคร','ชื่อ','ดื่ม','กลิ่น','รส',
    'รูป','สัมผัส','หวาน','เค็ม','เปรี้ยว',
    'เผ็ด','จืด','ชา','ขม','เคี้ยว',
    'ชาติ','ลาย','เต้น','หอม','เหม็น',
    'ฉุน','โกรธ','ชิน','เงียบ','ตะโกน',
    'รัฐ','ราช','รัฐบาล','เอกชน','ประชาชน',
    'บริษัท','ประชา','ชน','พรรค','สภา',
    'ตำรวจ','ทหาร','กองทัพ','ศาล','พิพากษา',
    'ข่าว','กฎ','ระเบียบ','หลัก','เกณฑ์',
    'ละเมิด','เสรี','สิทธิ','ทรัพย์','โทษ',
    ]

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_SECRET =''

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=THAI_COMMON_WORDS, languages=['th'])
