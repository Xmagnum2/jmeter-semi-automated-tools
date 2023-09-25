 // Java Import
import java.time.*
import java.time.format.*
import org.apache.jmeter.threads.JMeterContextService

// def testCaseCode = 
def threadGroupName = JMeterContextService.getContext().getThreadGroup().getName()
def threadNum = JMeterContextService.getContext().getThreadNum()
def loopCount = vars.get("iteration").toInteger()

// Acquiring the current time
def currZoneTime = DateTimeFormatter.ISO_OFFSET_DATE_TIME.format(ZonedDateTime.now())

// Start log
log.debug("[CHECK] currZoneTime = [${currZoneTime}] : threadGroupName = [${threadGroupName}] : threadNum = [${threadNum}] : loopCount = [${loopCount}]")

def size = vars.get("size").toInteger()

// Initializing working variables

// Assembling data
def jsonElement = """
{
  "size": ${size},
  "loopCount": ${loopCount}
}
"""

// Bind JSON data to the variable defined in HTTP Request Body
vars.put("jsonData", jsonElement)
