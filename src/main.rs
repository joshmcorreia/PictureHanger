struct PictureHanger {
    wall_width: f64,
    wall_offset: f64,
    num_pictures: i32,
    frame_width: f64,
    height_from_nail_to_top_of_picture: f64,
    desired_top_of_picture_height: f64,
    distance_between_frames: f64,
}

impl PictureHanger {
    fn height(&self) -> f64 {
        self.desired_top_of_picture_height - self.height_from_nail_to_top_of_picture
    }

    fn half_frame_width(&self) -> f64 {
        self.frame_width/2 as f64
    }

    fn outer_width(&self) -> f64 {
        (self.wall_width - ((self.frame_width * self.num_pictures as f64) + ((self.num_pictures - 1) as f64 * self.distance_between_frames)))/2 as f64
    }
}

fn main() {
    let picture_hanger = PictureHanger {
        wall_width: 1.602,
        wall_offset: 0.0,
        num_pictures: 3,
        frame_width: 0.433,
        height_from_nail_to_top_of_picture: 0.01,
        desired_top_of_picture_height: 1.786,
        distance_between_frames: 0.03,
    };

    let height = picture_hanger.height();
    let outer_width = picture_hanger.outer_width();

    if outer_width < 0 as f64 {
        let absolute_outer_width = outer_width.abs();
        println!("ERROR: This configuration of paintings does not fit on the wall. You would need {:.3}m more of wall space!", absolute_outer_width);
        return
    }

    let mut distance_from_wall: f64 = 0.0;
    for painting in 1..picture_hanger.num_pictures+1 {
        if painting == 1 {
            distance_from_wall = outer_width + picture_hanger.half_frame_width();
        }
        else {
            distance_from_wall = distance_from_wall + picture_hanger.frame_width + picture_hanger.distance_between_frames;
        }

        let distance_from_wall_with_offset = distance_from_wall + picture_hanger.wall_offset;

        if painting != 1 {
            println!();
        }
        println!("Painting {}:\nDistance from wall: {:.3}m\nDistance from ground: {:.3}m", painting, distance_from_wall_with_offset, height);
    }
}
