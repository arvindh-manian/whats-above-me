from typing import List, Tuple
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_moment import Moment
from datetime import date, datetime, timedelta

app = Flask(__name__)
bootstrap = Bootstrap5(app)
moment = Moment(app)

def get_cloud_cover(lat: float, long: float) -> int:
	return 55

def get_pressure(lat: float, long: float) -> int:
	return 800

def clean_timestamps(articles: List) -> None:
	for article in articles:
		article['updatedAt'] = datetime.fromisoformat(article['updatedAt'].strip('Z'))

def get_articles() -> List:
	articles = [{"id":16094,"title":"SpaceX fires up Starship booster at orbital launch pad","url":"https://www.teslarati.com/spacex-starship-booster-7-first-static-fire/","imageUrl":"https://www.teslarati.com/wp-content/uploads/2022/08/Super-Heavy-B7-Starbase-OLS-080922-SpaceX-static-fire-1-1-crop-c.jpg","newsSite":"Teslarati","summary":"For the first time, SpaceX has static fired a Starship booster at its South Texas orbital launch pad, marking important milestones for...","publishedAt":"2022-08-09T23:55:52.000Z","updatedAt":"2022-08-09T23:56:09.952Z","featured":False,"launches":[],"events":[]},{"id":16093,"title":"U.S. Space Command basing decision approaching final stretch","url":"https://spacenews.com/u-s-space-command-basing-decision-approaching-final-stretch/","imageUrl":"https://spacenews.com/wp-content/uploads/2022/08/Screen-Shot-2022-08-09-at-12.59.01-PM.png","newsSite":"SpaceNews","summary":"The head of U.S. Space Command said he expects a final decision to be made relatively soon on where the command will be permanently headquartered.","publishedAt":"2022-08-09T22:25:19.000Z","updatedAt":"2022-08-09T22:25:19.908Z","featured":False,"launches":[],"events":[]},{"id":16092,"title":"D-Orbit to deploy 20 Astrocast satellites over three years","url":"https://spacenews.com/d-orbit-to-deploy-20-astrocast-satellites-over-three-years/","imageUrl":"https://spacenews.com/wp-content/uploads/2022/08/D-Orbit.jpg","newsSite":"SpaceNews","summary":"Italy’s D-Orbit said Aug. 9 that it would launch 20 nanosatellites over three years for Swiss startup Astrocast with its orbital transfer vehicle.","publishedAt":"2022-08-09T22:05:33.000Z","updatedAt":"2022-08-09T22:05:33.825Z","featured":False,"launches":[],"events":[]},{"id":16087,"title":"Aerospace develops low-cost optical ground network","url":"https://spacenews.com/aerospace-optical-ground/","imageUrl":"https://spacenews.com/wp-content/uploads/2022/08/rsz_aerospace_dome.jpg","newsSite":"SpaceNews","summary":"The Aerospace Corp. is establishing a network of remotely operated optical communications terminals to support existing and future small satellite missions.","publishedAt":"2022-08-09T21:35:27.000Z","updatedAt":"2022-08-09T21:35:27.552Z","featured":False,"launches":[],"events":[]},{"id":16090,"title":"Maxar to supply 14 satellites for U.S. military missile-tracking constellation","url":"https://spacenews.com/maxar-to-supply-14-satellites-for-u-s-military-missile-tracking-constellation/","imageUrl":"https://spacenews.com/wp-content/uploads/2022/08/MAXAR-011-025_10.jpg","newsSite":"SpaceNews","summary":"Maxar Technologies announced Aug. 9 it was selected by L3Harris to manufacture 14 missile-detection satellites for the U.S. Space Development Agency.","publishedAt":"2022-08-09T21:35:27.000Z","updatedAt":"2022-08-09T21:35:27.426Z","featured":False,"launches":[],"events":[]},{"id":16080,"title":"Sidus Space could launch LizzieSat-1 without thrusters","url":"https://spacenews.com/sidus-space-mulls-rideshare-mission-for-debut-satellite/","imageUrl":"https://spacenews.com/wp-content/uploads/2022/01/Orbitplex_072621-6-1.jpg","newsSite":"SpaceNews","summary":"Sidus Space could launch LizzieSat-1 without thrusters if it can’t get safety clearances in time to deploy its first satellite from the International Space Station early next year.","publishedAt":"2022-08-09T20:55:24.000Z","updatedAt":"2022-08-09T20:55:24.553Z","featured":False,"launches":[],"events":[]},{"id":16088,"title":"Starlink Group 4-26 slated for Tuesday launch from LC-39A","url":"https://www.nasaspaceflight.com/2022/08/starlink-4-26/","imageUrl":"https://www.nasaspaceflight.com/wp-content/uploads/2022/08/IXPE_Julia-1170x847.jpg","newsSite":"NASA Spaceflight","summary":"On August 9 at 6:57 PM EDT (22:57 UTC), SpaceX’s Falcon 9 rocket will lift off from pad 39A at the Kennedy Space Center, carrying 52 Starlink satellites to Low Earth Orbit (LEO). These satellites will contribute to filling up the fourth shell of the Starlink constellation, which is now available in 36 countries to provide internet access to people around the globe.","publishedAt":"2022-08-09T20:43:26.000Z","updatedAt":"2022-08-09T20:49:09.807Z","featured":False,"launches":[{"id":"a6b9deb4-f78d-4b57-8e47-98c5aea99d9e","provider":"Launch Library 2"}],"events":[]},{"id":16086,"title":"China’s secretive space plane flies higher and longer than before","url":"https://arstechnica.com/science/2022/08/chinas-secretive-space-plane-flies-higher-and-longer-than-before/","imageUrl":"https://cdn.arstechnica.net/wp-content/uploads/2022/08/GettyImages-1401280831.jpg","newsSite":"Arstechnica","summary":"So what is it doing up there? Secret, space-y stuff, of course.","publishedAt":"2022-08-09T20:06:51.000Z","updatedAt":"2022-08-09T20:15:55.971Z","featured":False,"launches":[{"id":"4edae34f-34fc-4b80-b806-23c242fa2ad6","provider":"Launch Library 2"}],"events":[]},{"id":16085,"title":"SpaceX sees continued strong demand for rideshare missions","url":"https://spacenews.com/spacex-sees-continued-strong-demand-for-rideshare-missions/","imageUrl":"https://spacenews.com/wp-content/uploads/2022/05/transporter5.jpg","newsSite":"SpaceNews","summary":"SpaceX, whose rideshare services have reshaped the smallsat launch market, says it continues to see strong demand with missions booked into 2025.","publishedAt":"2022-08-09T20:05:13.000Z","updatedAt":"2022-08-09T20:05:13.576Z","featured":False,"launches":[],"events":[]},{"id":16082,"title":"Atlas Space Operations upgrades user interface to ease scheduling","url":"https://spacenews.com/atlas-user-interface/","imageUrl":"https://spacenews.com/wp-content/uploads/2022/08/rsz_screen_shot_2022-08-08_at_13543_pm.png","newsSite":"SpaceNews","summary":"Atlas Space Operations upgraded its user interface to make it easier for customers to schedule communications with their satellites and to quickly confirm whether data was transmitted.","publishedAt":"2022-08-09T19:15:28.000Z","updatedAt":"2022-08-09T19:15:29.053Z","featured":False,"launches":[],"events":[]}]
	clean_timestamps(articles)
	return articles

def get_twilight() -> Tuple[datetime, datetime]:
	return datetime.utcnow(), datetime.utcnow() + timedelta(hours=2)

def eval_stargaze(cloud_cover: int, twilight_start: datetime, twilight_end: datetime) -> bool:
	return True

@app.route('/')
def index():
	cloud_cover = get_cloud_cover(lat=0, long=0)
	pressure = get_pressure(lat=0, long=0)
	articles = get_articles()
	twilight_start, twilight_end = get_twilight()
	should_stargaze = eval_stargaze(cloud_cover=cloud_cover, twilight_start=twilight_start, twilight_end=twilight_end)
	return render_template('index.html', pressure=pressure, should_stargaze=should_stargaze, cloud_cover=cloud_cover, twilight_start=twilight_start, twilight_end=twilight_end, articles=articles)