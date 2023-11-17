import sys
import yaml

class PictureHanger:
	def __init__(self) -> None:
		self.config_file_name = "config.yaml"
		self.parse_config_file()


	def parse_config_file(self) -> None:
		"""
		Parses config.yml
		"""
		yaml_dictionary = {}
		with open(self.config_file_name, "r") as file_in:
			yaml_dictionary = yaml.safe_load(file_in)

		self.decimal_precision = 3

		self.wall_width = yaml_dictionary["wall_width"]
		self.wall_offset = yaml_dictionary["wall_offset"]
		self.frame_width = yaml_dictionary["frame_width"]
		self.half_frame_width = self.frame_width/2
		self.num_pictures = yaml_dictionary["num_pictures"]
		self.height_from_nail_to_top_of_picture = yaml_dictionary["height_from_nail_to_top_of_picture"]
		self.desired_top_of_picture_height = yaml_dictionary["desired_top_of_picture_height"]
		if self.num_pictures == 1:
			self.distance_between_frames = 0
		else:
			self.distance_between_frames = yaml_dictionary["distance_between_frames"]


	def calculate_height(self) -> float:
		return self.desired_top_of_picture_height - self.height_from_nail_to_top_of_picture


	def calculate_locations(self) -> None:
		height = self.calculate_height()
		outer_width = (self.wall_width - ((self.frame_width * self.num_pictures) + ((self.num_pictures - 1) * self.distance_between_frames)))/2

		if outer_width < 0:
			absolute_outer_width = abs(outer_width)
			print(f"ERROR: This configuration of paintings does not fit on the wall. You would need {round(absolute_outer_width, self.decimal_precision)}m more of wall space!")
			sys.exit(1)

		for painting in range(1, self.num_pictures + 1):
			if painting == 1:
				distance_from_wall = outer_width + self.half_frame_width
			else:
				distance_from_wall = distance_from_wall + self.frame_width + self.distance_between_frames

			distance_from_wall_with_offset = distance_from_wall + self.wall_offset

			if painting != 1: # split each section with a newline
				print()
			print(f"Painting {painting}:\nDistance from wall: {round(distance_from_wall_with_offset, self.decimal_precision)}m\nDistance from ground: {round(height, self.decimal_precision)}m")


def main():
	picture_hanger = PictureHanger()
	picture_hanger.calculate_locations()


if __name__ == "__main__":
	main()
