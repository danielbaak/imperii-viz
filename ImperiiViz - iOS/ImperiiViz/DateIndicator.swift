//
//  DateIndicator.swift
//  ImperiiViz
//
//  Created by Frederik Riedel on 26.04.15.
//  Copyright (c) 2015 Frederik Riedel. All rights reserved.
//

import UIKit

class DateIndicator: UIView {
    
    var dateLabel : UILabel?
    
    override init(frame: CGRect) {
        super.init(frame: frame)
        
        var imageView = UIImageView(frame: CGRectMake(0, 0, self.frame.width, self.frame.height))
        imageView.image=UIImage(named: "Annotation")
        self.addSubview(imageView)
        
        dateLabel = UILabel(frame: CGRectMake(0, 0, self.frame.width, 0.75 * self.frame.height))
        dateLabel?.font = UIFont(name: "Helveticaneue", size: 25)
        dateLabel?.textAlignment=NSTextAlignment.Center
        self.addSubview(dateLabel!)
    }

    required init(coder aDecoder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    
    func setYear(year: Float) {
        self.dateLabel?.text=String(Int(year))
    }

    /*
    // Only override drawRect: if you perform custom drawing.
    // An empty implementation adversely affects performance during animation.
    override func drawRect(rect: CGRect) {
        // Drawing code
    }
    */

}
